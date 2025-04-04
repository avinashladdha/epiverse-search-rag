import os
from pathlib import Path
import shutil
import pandas as pd
import time
from nltk import sent_tokenize
from sentence_transformers import SentenceTransformer
import torch
import glob
import yaml
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import azure.functions as func
import logging.config
from logging.handlers import RotatingFileHandler
import nltk
nltk.download('punkt_tab')

with open('logging_config.yaml', 'r') as f:
    config = yaml.safe_load(f)

logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

# --- Configuration ---
SOURCE_FOLDER = '/sources/'
OUTPUT_EMBEDDINGS_PATH = 'corpus_embeddings.pth'
OUTPUT_ANALYSIS_DF_PATH = 'analysis_df.csv'
BI_ENCODER_MODEL = 'multi-qa-MiniLM-L6-cos-v1' # map queries and documents into a dense vector space such that relevant pairs have high cosine similarity. Works with Cross encoder in API file
MAX_SEQ_LENGTH = 256
WINDOW_SIZE = 7
MIN_SENTENCE_TOKENS = 5
DEVICE = torch.device("cpu")


# --- Utility Functions ---
def read_md_files_from_subfolders(folder_path: str) -> dict:
    """Reads .md files from subfolders, excluding those in 'vignettes/man'.
       Args:
           folder_path: The path to the folder containing .md files.
       Returns:
           A dict where keys are subfolder names and values are lists of
           (filename, content) tuples.
    """
    folder = Path(folder_path)
    file_data = {}
    md_files = [
        f for f in glob.iglob(f"{folder}/**/*.md", recursive=True)
        if "vignettes/man" not in Path(f).as_posix()
    ]

    print(len(md_files))
    logger.info(f"Found {len(md_files)} files to process.")
    for md_file in md_files:
        path_obj = Path(md_file)
        try:
            subfolder = path_obj.parent.name
            folder_name = path_obj.parent.parent.name
            with open(path_obj, 'r', encoding='utf-8') as file:
                content = file.read()
            if folder_name not in file_data:
                file_data[folder_name] = []
            file_data[folder_name].append((path_obj.name, content))
        except Exception as e:
            logger.error(f"Could not read {md_file}: {e}")
    logger.info(f"Successfully read data from {len(file_data)} subfolders.")
    return file_data



def preprocess_content(content: str) -> list[list[str]]:
    """Cleans and tokenizes content into sentences.
    Args:
        content: The text content to preprocess.

    Returns:
        A list of lists, where each inner list contains sentences (list of string).
    """
    cleaned_content = content.replace("\r\n", "\n").replace("\n", "").replace("#", "").replace("*", "")
    paragraphs = cleaned_content.split("\n\n")
    sentences = []
    for paragraph in paragraphs:
        if paragraph.strip():
            sents = sent_tokenize(paragraph.strip())
            filtered_sents = [sent for sent in sents if len(sent.split()) >= MIN_SENTENCE_TOKENS]
            if filtered_sents:
                sentences.append(filtered_sents)
    return sentences



def create_document_list(file_data: dict) -> list[dict]:
    """Creates a list of dictionaries, each representing a document
    with metadata and tokenized content.

    Args:
        file_data: A dictionary containing file data, as returned by
        read_md_files_from_subfolders.

    Returns:
        A list of dictionaries, where each dictionary has keys
        'package_name', 'file_name', 'content', and 'tokenized_content'.
    """
    doc_list = []
    for subfolder, files in file_data.items():
        for file_name, content in files:
            tokenized_content = preprocess_content(content)
            if tokenized_content:
                temp_dict = {
                    'package_name': subfolder,
                    'file_name': file_name,
                    'content': content,
                    'tokenized_content': tokenized_content
                }
                doc_list.append(temp_dict)
    logger.info(
        f"Created a document list containing {len(doc_list)} documents.")
    return doc_list



def create_analysis_dataframe(doc_list: list[dict], window_size: int) -> pd.DataFrame:
    """Creates and preprocesses the analysis DataFrame.

    Args:
        doc_list: A list of document dictionaries.
        window_size: The window size for grouping sentences.

    Returns:
        A Pandas DataFrame with columns 'package_name', 'file_name',
        'content', 'tokenized_content', 'sentence_count', 'content_cleaned',
        and 'cluster_id'.
    """
    analysis_df = pd.DataFrame(doc_list)

    analysis_df['sentence_count'] = analysis_df['tokenized_content'].apply(len)
    analysis_df['content_cleaned'] = analysis_df['content'].apply(lambda x: x.replace('\n', '').replace("#", "").replace("*", ""))
    analysis_df_exploded = analysis_df.explode("tokenized_content")
    analysis_df_exploded['tokenized_content'] = analysis_df_exploded['tokenized_content'].apply(lambda x: str(x))
    analysis_df_exploded['cluster_id'] = [i // window_size for i in range(len(analysis_df_exploded))]

    logger.info(
        f"Created analysis DataFrame with {len(analysis_df_exploded)} rows of tokenized content.")

    return analysis_df_exploded



def create_passages(analysis_df: pd.DataFrame, window_size: int) -> list[str]:
    """Creates passages by joining tokenized content within a sliding window.

    Args:
        analysis_df: The analysis DataFrame.
        window_size: The number of sentences to combine into a passage.

    Returns:
        A list of strings, where each string is a passage.
    """
    paragraphs = analysis_df['tokenized_content'].tolist()
    passages = []
    for i in range(0, len(paragraphs), window_size):
        window = paragraphs[i:i + window_size]
        passages.append("; ".join(window))
    return passages



def encode_and_save_embeddings(passages: list[str], output_path: str,
                              model_name: str, max_length: int,
                              device: DEVICE) -> None:
    """Encodes passages using a SentenceTransformer and saves the embeddings.

    Args:
        passages: A list of text passages.
        output_path: The path to save the embeddings.
        model_name: The name of the SentenceTransformer model.
        max_length: The maximum sequence length for the model.
        device: The torch device to use (e.g., 'cpu' or 'cuda').
    """
    bi_encoder = SentenceTransformer(model_name)
    bi_encoder.max_seq_length = max_length
    corpus_embeddings = bi_encoder.encode(passages, convert_to_tensor=True,
                                          device=DEVICE)
    torch.save(corpus_embeddings, output_path)

    logger.info(f"Embeddings saved to '{output_path}' with shape: {corpus_embeddings.shape}.")


# --- Main Execution ---
def main(mytimer: func.TimerRequest) -> None:
    start_time = time.time()

    logger.info("--- Starting the document processing pipeline ---")
    file_data = read_md_files_from_subfolders(SOURCE_FOLDER)

    logger.info("--- Creating Document List and Tokenizing Content ---")
    doc_list = create_document_list(file_data)

    analysis_df = create_analysis_dataframe(doc_list, WINDOW_SIZE)

    passages = create_passages(analysis_df, WINDOW_SIZE)

    encode_and_save_embeddings(passages, OUTPUT_EMBEDDINGS_PATH,
                              BI_ENCODER_MODEL, MAX_SEQ_LENGTH, DEVICE)


    analysis_df.to_csv(OUTPUT_ANALYSIS_DF_PATH, index=False)
    logger.info(
    f"Analysis DataFrame saved to '{OUTPUT_ANALYSIS_DF_PATH}' with {len(analysis_df)} rows and {len(analysis_df.columns)} columns.")

    end_time = time.time()
    total_time = end_time - start_time
    logger.info(f"--- Finished processing in {total_time:.2f} seconds ---")
