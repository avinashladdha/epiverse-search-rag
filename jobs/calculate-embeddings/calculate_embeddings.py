from pathlib import Path
import pandas as pd
import time
from nltk import sent_tokenize
from sentence_transformers import SentenceTransformer
import torch
import glob
import yaml
import subprocess
import logging.config
import tempfile

with open('logging_config.yaml', 'r') as f:
    config = yaml.safe_load(f)

logging.config.dictConfig(config)
logger = logging.getLogger(__name__)

# --- Configuration ---
tmpdir = tempfile.TemporaryDirectory(prefix = "sources_")
SOURCE_FOLDER = tmpdir.name
BI_ENCODER_MODEL = 'multi-qa-MiniLM-L6-cos-v1' # map queries and documents into a dense vector space such that relevant pairs have high cosine similarity. Works with Cross encoder in API file
MAX_SEQ_LENGTH = 256
WINDOW_SIZE = 7
MIN_SENTENCE_TOKENS = 5
DEVICE = torch.device("cpu")

# --- Utility Functions ---
def get_universe_docs(universe: str, destdir: str) -> None:
    try:
        subprocess.run(
            ["Rscript", "-e", f"epiverse.scraper::get_universe_docs('{universe}', '{destdir}')"],
            check=True,
            capture_output=True,
            text=True
        )
        logging.info("R script ran successfully\n")
    except subprocess.CalledProcessError as e:
        error = RuntimeError("Error running R script:\n" + e.stderr)
        logging.error(error)
        raise error

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

    # Vignettes can be:
    # - simple markdown files (.md)
    # - Rmarkdown files (.Rmd)
    # - quarto files (.qmd)
    # All these formats are based on markdown and can be parsed as plain text.
    md_files = [
        f for f in glob.iglob(f"{folder}/**/*md", recursive=True)
        if "vignettes/man" not in Path(f).as_posix()
          and f.endswith((".Rmd", ".md", ".qmd"))
    ]

    print(len(md_files))
    logger.info(f"Found {len(md_files)} files to process.")
    for md_file in md_files:
        path_obj = Path(md_file)
        try:
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
    cleaned_content = content.replace("\r\n", "\n").replace("\n", " ").replace("#", "").replace("*", "")
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
        'tokenized_content' and 'cluster_id'.
    """
    analysis_df = pd.DataFrame(doc_list)

    analysis_df_exploded = analysis_df.explode("tokenized_content")
    analysis_df_exploded['tokenized_content'] = analysis_df_exploded['tokenized_content'].apply(lambda x: str(x))
    # Generate cluster_id
    cluster_ids = []
    current_cluster = 0

    for package_name, group in analysis_df_exploded.groupby("package_name", sort=False):
        n = len(group)
        # Assign a cluster_id every `window_size` rows in the group
        for i in range(n):
            cluster_ids.append(current_cluster + (i // window_size))
        current_cluster = cluster_ids[-1] + 1  # Prepare for next package

    analysis_df_exploded["cluster_id"] = cluster_ids
    analysis_df_exploded = analysis_df_exploded[['package_name', 'file_name', 'tokenized_content', 'cluster_id']]

    logger.info(
        f"Created analysis DataFrame with {len(analysis_df_exploded)} rows of tokenized content.")

    return analysis_df_exploded




def create_passages(analysis_df: pd.DataFrame) -> list[str]:
    """Creates passages by joining tokenized content within a sliding window.

    Args:
        analysis_df: The analysis DataFrame.

    Returns:
        A list of strings, where each string is a passage.
    """

    cluster_count = analysis_df['cluster_id'].nunique()

    passages = []
    for i in range(0, cluster_count):
        window = analysis_df[analysis_df['cluster_id']==i]['tokenized_content'].tolist()
        passages.append('; '.join(window))
    return passages



def encode_embeddings(passages: list[str],
                      model_name: str, max_length: int,
                      device: DEVICE) -> None:
    """Encodes passages using a SentenceTransformer and returns the embeddings.

    Args:
        passages: A list of text passages.
        model_name: The name of the SentenceTransformer model.
        max_length: The maximum sequence length for the model.
        device: The torch device to use (e.g., 'cpu' or 'cuda').
    """
    bi_encoder = SentenceTransformer(model_name)
    bi_encoder.max_seq_length = max_length
    corpus_embeddings = bi_encoder.encode(passages, convert_to_tensor=True,
                                          device=DEVICE)
    return corpus_embeddings


# --- Main Execution ---
def fetch_docs_and_embed(universe: str = "epiverse-connect"):
    start_time = time.time()

    logger.info("--- Fetching the documentation files ---")
    get_universe_docs(universe, SOURCE_FOLDER)

    logger.info("--- Starting the document processing pipeline ---")
    file_data = read_md_files_from_subfolders(SOURCE_FOLDER)

    logger.info("--- Creating Document List and Tokenizing Content ---")
    doc_list = create_document_list(file_data)

    analysis_df = create_analysis_dataframe(doc_list, WINDOW_SIZE)

    passages = create_passages(analysis_df)

    corpus_embeddings = encode_embeddings(passages, BI_ENCODER_MODEL, MAX_SEQ_LENGTH, DEVICE)

    end_time = time.time()
    total_time = end_time - start_time
    logger.info(f"--- Finished processing in {total_time:.2f} seconds ---")

    return analysis_df, corpus_embeddings
