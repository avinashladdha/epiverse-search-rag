import os
from pathlib import Path
from transformers import AutoTokenizer, AutoModel
import torch
import shutil
import pandas as pd
import time
from nltk import sent_tokenize
from sentence_transformers import SentenceTransformer, CrossEncoder, util
device = torch.device("cpu")
import string
import numpy as np
import pickle

# Functions

def read_md_files_from_subfolders(folder_path):
    # Use Path from pathlib to manage paths
    folder = Path(folder_path)

    # Create a dictionary to store subfolder names and file contents
    file_data = {}
    # Get all .md files from subfolders recursively
    md_files = [i for i in Path(folder_path).glob('**/*.R?md') if not ('vignettes/man' in str(i) or 'vignettes\\man' in str(i))]

    # Iterate through each file and read content
    for md_file in md_files:
        try:
            # Extract the subfolder name
            subfolder = md_file.parent.name
            folder_name = md_file.parent.parent.name
            # Open and read the .md file
            with open(md_file, 'r', encoding='utf-8') as file:
                content = file.read()

                # Store the content under the subfolder key
                if folder_name not in file_data:
                    file_data[folder_name] = []

                # Append a tuple (filename, content) to the subfolder entry
                file_data[folder_name].append((md_file.name, content))
        except Exception as e:
            print(f"Could not read {md_file}: {e}")
    return file_data


file_data = read_md_files_from_subfolders('./sources/')

# Display the results
for subfolder, files in file_data.items():
    print(f"Subfolder: {subfolder}")
    for file_name, content in files:
        try:
            print(f"  File: {file_name}, Content: {content[5]}...")  # Display first 100 characters for brevity
        except:
            print("error for - {}".format(file_name))

doc_list = []
for subfolder, files in file_data.items():
    for file_name, content in files:
        paragraphs = []
        for paragraph in content.replace("\r\n", "\n").split("\n\n"):
            if len(paragraph.strip()) > 0:
                paragraph = paragraph.replace("\n","").replace("#","")
                paragraphs.append(sent_tokenize(paragraph.strip()))
                # Append the dictionary to the list
        filtered_paragraphs = [lst for lst in paragraphs if len(str(lst).split(' ')) >= 5]
        temp_dict = {
        'package_name': subfolder,
        'file_name': file_name,
        'content': content,
        'tokenized_content' : filtered_paragraphs
        }
        doc_list.append(temp_dict)



temp_df = pd.DataFrame(doc_list)
temp_df['cc'] = temp_df['tokenized_content'].apply(lambda x :len(x))
temp_df['content_cleaned'] = temp_df['content'].apply(lambda x : x.replace('\n','').replace("#","").replace("*",""))

analysis_df = temp_df.explode("tokenized_content")
analysis_df['tokenized_content'] = analysis_df['tokenized_content'].apply(lambda x : str(x)[2:-2])
analysis_df['cluster_id'] = [i//window_size for i in range(len(analysis_df))]

# Break down the content into smaller chunks
# WIndow size is = 7 as this was the median length of documents in the dataset
paragraphs = analysis_df['tokenized_content'].to_list()
# Smaller value: Context from other sentences might get lost
# Lager values: More context from the paragraph remains, but results are longer
window_size = 7
passages= []

for start_idx in range(0, len(paragraphs), window_size):
    end_idx = min(start_idx + window_size, len(paragraphs))
    passages.append(";".join(paragraphs[start_idx:end_idx]))


#We use the Bi-Encoder to encode all passages, so that we can use it with semantic search
bi_encoder = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
bi_encoder.max_seq_length = 256    #Truncate long passages to 256 tokens
top_k = 32                          #Number of passages we want to retrieve with the bi-encoder

#The bi-encoder will retrieve 32 documents. We use a cross-encoder, to re-rank the results list to improve the quality
cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# We encode all passages into our vector space.
corpus_embeddings = bi_encoder.encode(passages, convert_to_tensor=True, show_progress_bar=True)

torch.save(corpus_embeddings,"./app/corpus_embeddings.pth")
print("Embeddings saved to 'embeddings.pth'.")
analysis_df.to_csv('./app/analysis_df.csv', index = False)
