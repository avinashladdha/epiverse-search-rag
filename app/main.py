from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from models import SearchResponse
from search_engine import SemanticSearchEngine
import logging

# --- Logging Configuration ---
log_file_path = "query_and_response.log"  # Define the log file path
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



app = FastAPI(debug=True)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "epiverse-connect.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the search engine when the app starts
search_engine = SemanticSearchEngine(
    corpus_embeddings_path="../data/corpus_embeddings.pth",
    analysis_df_path="../data/analysis_df.csv",
    package_descr_path="../data/epipkgs_metadata.json",
    device="cpu" # Or "cuda" if available
)

@app.get("/api/", response_model=SearchResponse)
def get_data(query: str = Query(..., description="User query string")):
    logger.info("Input question:{query}")
    results = search_engine.search(query)
    json_response = {
        "query": query,
        "filter": "epiverse",
        "response": {
            "results": results,
        }
    }
    logger.info("Response:{json_response}")
    return json_response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)