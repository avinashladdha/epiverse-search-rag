import torch
from sentence_transformers import SentenceTransformer, CrossEncoder, util
import pandas as pd
import logging

# --- Logging Configuration ---
log_file_path = "search_engine.log"  # Define the log file path
# Create a rotating file handler
log_handler = logging.handlers.RotatingFileHandler(
    log_file_path, maxBytes=10 * 1024 * 1024, backupCount=5)  # 10MB max, 5 backups)
# Create a formatter
log_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s")
# Set the formatter for the handler
log_handler.setFormatter(log_formatter)
# Get the root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Set the logging level for the logger
# Add the handler to the logger
logger.addHandler(log_handler)




class SemanticSearchEngine:
    def __init__(self, corpus_embeddings_path: str, analysis_df_path: str, package_descr_path: str, device: str = "cpu"):

        self.corpus_embeddings = torch.load(corpus_embeddings_path, map_location=torch.device(device))
        logger.info("Loaded embeddings.")
        self.bi_encoder = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
        self.bi_encoder.max_seq_length = 256
        self.cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
        self.analysis_df = pd.read_csv(analysis_df_path)
        package_descr_df = pd.read_json(package_descr_path, dtype=str)
        package_descr_df = package_descr_df.map(lambda x: str(x)[2:-2])
        self.analysis_df = self.analysis_df.merge(package_descr_df, left_on='package_name', right_on='package', how='left')
        self.paragraphs = [str(s) for s in self.analysis_df['tokenized_content'].to_list()]
        self.window_size = 7
        self.passages = self._create_passages()
        self.device = torch.device(device)

    def _create_passages(self):
        passages = []
        for start_idx in range(0, len(self.paragraphs), self.window_size):
            end_idx = min(start_idx + self.window_size, len(self.paragraphs))
            passages.append(";".join(self.paragraphs[start_idx:end_idx]))
        return passages

    def search(self, query: str, top_k: int = 32, num_results: int = 5):
        question_embedding = self.bi_encoder.encode(query, convert_to_tensor=True).to(self.device)
        hits = util.semantic_search(question_embedding, self.corpus_embeddings, top_k=top_k)[0]

        cross_inp = [[query, self.passages[hit['corpus_id']]] for hit in hits]
        cross_scores = self.cross_encoder.predict(cross_inp)

        for idx in range(len(cross_scores)):
            hits[idx]['cross-score'] = cross_scores[idx]

        hits = sorted(hits, key=lambda x: x['cross-score'], reverse=True)

        hits_df = pd.DataFrame(hits).head(20)

        merged_df = pd.merge(hits_df, self.analysis_df, left_on='corpus_id', right_on='cluster_id', how='left')
        merged_df = merged_df.drop_duplicates(subset=['package_name'], keep='first')
        merged_df = merged_df.drop(columns=['corpus_id', 'cluster_id', 'score',
                                            'tokenized_content', 'file_name'
                                            ], axis=1)
        merged_df['cross-score'] = merged_df['cross-score'].apply(lambda x : round(x, 4))
        # Rename specific columns using a dictionary
        new_columns = {'cross-score': 'relevance'}
        merged_renamed = merged_df.rename(columns=new_columns)

        # Sort by relevance and Remove duplicates
        results_df = merged_renamed.sort_values(by='relevance', ascending=False).drop_duplicates(subset=['package_name'], keep='first')
        results_df = results_df.fillna('')

        return results_df.to_dict('records')
