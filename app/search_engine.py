import torch
from sentence_transformers import SentenceTransformer, CrossEncoder, util
import pandas as pd
from utils import get_value



# --- Logging Configuration ---
log_file_path = "search_engine.log"  # Define the log file path
# Create a rotating file handler
log_handler = RotatingFileHandler(
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
        package_descr_df.columns = ['package', 'logo', 'website', 'source', 'articles']
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
        results = []
        for hit in hits[:20]:
            package_name = get_value(self.analysis_df, 'package_name', self.analysis_df['cluster_id'] == hit['corpus_id'])
            logo = get_value(self.analysis_df, 'logo', self.analysis_df['cluster_id'] == hit['corpus_id'])
            website = get_value(self.analysis_df, 'website', self.analysis_df['cluster_id'] == hit['corpus_id'])
            source_package = get_value(self.analysis_df, 'source', self.analysis_df['cluster_id'] == hit['corpus_id'])
            vignettes = ["To be added to scrapper"]
            if package_name:
                results.append({
                    "package_name": package_name,
                    "logo": logo,
                    "website": website,
                    "source": source_package,
                    "vignettes": vignettes,
                    "relevance": round(hit['score'], 4),
                })

        # Remove duplicates and sort by relevance
        results_df = pd.DataFrame(results).drop_duplicates(subset=['package_name'], keep='first')
        results_df = results_df.sort_values(by='relevance', ascending=False).head(num_results)
        return results_df.to_dict('records')
