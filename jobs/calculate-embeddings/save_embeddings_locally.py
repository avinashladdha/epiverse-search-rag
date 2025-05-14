import torch
import logging
import sys
from calculate_embeddings import fetch_docs_and_embed

OUTPUT_EMBEDDINGS_PATH = 'corpus_embeddings.pth'
OUTPUT_ANALYSIS_DF_PATH = 'analysis_df.csv'

if __name__ == "__main__":
    # universe of interest can potentially be passed as command line arg
    arg = sys.argv[1] if len(sys.argv) > 1 else None

    if arg is not None:
        logging.info(f"Calling fetch_docs_and_embed() for universe {arg}")
        analysis_df, corpus_embeddings = fetch_docs_and_embed(arg)
    else:
        logging.info("Calling fetch_docs_and_embed() for universe epiverse-connect.")
        analysis_df, corpus_embeddings = fetch_docs_and_embed()

    torch.save(corpus_embeddings, OUTPUT_EMBEDDINGS_PATH)
    logging.info(f"Embeddings saved to '{OUTPUT_EMBEDDINGS_PATH}' with shape: {corpus_embeddings.shape}.")

    analysis_df.to_csv(OUTPUT_ANALYSIS_DF_PATH, index=False)
    logging.info(
    f"Analysis DataFrame saved to '{OUTPUT_ANALYSIS_DF_PATH}' with {len(analysis_df)} rows and {len(analysis_df.columns)} columns.")
