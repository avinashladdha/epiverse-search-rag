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
        self.analysis_df = self.analysis_df.merge(package_descr_df, left_on='package_name', right_on='package', how='left')
        self.paragraphs = [str(s) for s in self.analysis_df['tokenized_content'].to_list()]
        self.window_size = 7
        self.passages = self._create_passages()
        self.device = torch.device(device)

    def _create_passages(self):
        # Fix: Reconstruct passages using cluster_id to ensure alignment with embeddings
        # The logic must match calculate_embeddings.py exactly
        logger.info("Reconstructing passages using cluster_id...")
        
        # Ensure the DataFrame is sorted by cluster_id to strictly match embedding order
        # We must filter/sort to get the unique passages in order 0, 1, 2...
        
        # Group by cluster_id and join tokenized_content
        # Note: tokenized_content in the CSV is a string representation of the list
        # But we need to join the items in that list (sentences) or just join the cells?
        # In calculate_embeddings.py: 
        #   window = analysis_df[analysis_df['cluster_id']==i]['tokenized_content'].tolist()
        #   passages.append('; '.join(window))
        # Here, 'tokenized_content' seems to be individual sentences/chunks in the exploded view in calculate_embeddings
        # But let's check what analysis_df is in search_engine.
        
        passages = []
        # Get unique cluster IDs in sorted order
        unique_clusters = sorted(self.analysis_df['cluster_id'].unique())
        
        for cluster_id in unique_clusters:
            # Get all rows for this cluster, maintaining original order
            cluster_rows = self.analysis_df[self.analysis_df['cluster_id'] == cluster_id]
            # Join the content chunks
            # Assuming 'tokenized_content' column holds the text chunks
            chunk_content = cluster_rows['tokenized_content'].astype(str).tolist()
            passages.append(";".join(chunk_content))
            
        logger.info("Length of passages: %d", len(passages))    
        return passages

    def search(self, query: str, top_k: int = 20, num_results: int = 5):
        question_embedding = self.bi_encoder.encode(query, convert_to_tensor=True).to(self.device)
        hits = util.semantic_search(question_embedding, self.corpus_embeddings, top_k=top_k)[0]
        print(("Length of hits: %d", len(hits)) )
        logger.info("Length of hits: %d", len(hits))   
        cross_inp = [[query, self.passages[hit['corpus_id']]] for hit in hits]
        cross_scores = self.cross_encoder.predict(cross_inp)

        for idx in range(len(cross_scores)):
            hits[idx]['cross-score'] = cross_scores[idx]

        hits = sorted(hits, key=lambda x: x['cross-score'], reverse=True)

        hits_df = pd.DataFrame(hits).head(20)
        
        # Add content from passages
        hits_df['content'] = hits_df['corpus_id'].apply(lambda x: self.passages[int(x)])

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