import torch
import logging
from calculate_embeddings import fetch_docs_and_embed

OUTPUT_EMBEDDINGS_PATH = 'corpus_embeddings.pth'
OUTPUT_ANALYSIS_DF_PATH = 'analysis_df.csv'

if __name__ == "__main__":
    analysis_df, corpus_embeddings = fetch_docs_and_embed()

    torch.save(corpus_embeddings, OUTPUT_EMBEDDINGS_PATH)
    logging.info(f"Embeddings saved to '{OUTPUT_EMBEDDINGS_PATH}' with shape: {corpus_embeddings.shape}.")

    analysis_df.to_csv(OUTPUT_ANALYSIS_DF_PATH, index=False)
    logging.info(
    f"Analysis DataFrame saved to '{OUTPUT_ANALYSIS_DF_PATH}' with {len(analysis_df)} rows and {len(analysis_df.columns)} columns.")
