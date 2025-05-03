from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app.models import SearchResponse
from app.search_engine import SemanticSearchEngine
from app.utils import load_data_from_blob
import json
import logging
import os


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



# Global variable for search engine
search_engine = None

# Initialize search engine during app startup
@app.on_event("startup")
async def initialize_search_engine():
    global search_engine
    try:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(base_dir, "data")
        use_azure_storage = os.getenv("USE_AZURE_STORAGE", "false").lower() == "true"

        if use_azure_storage:
            logger.info("Loading data from Azure Blob Storage...")
            # TODO: pass the container name and blob name as environment variables
            corpus_embeddings_path = load_data_from_blob("data","corpus_embeddings.pth", "torch")
            analysis_df_path = load_data_from_blob("data", "analysis_df.csv","csv")
            package_descr_path = load_data_from_blob("data","epipkgs_metadata.json","json")
        else:
            logger.info("Loading data from local filesystem...")
            # TODO: pass file name as environment variable
            corpus_embeddings_path = os.path.join(data_dir, "corpus_embeddings.pth")
            analysis_df_path = os.path.join(data_dir, "analysis_df.csv")
            package_descr_path = os.path.join(data_dir, "epipkgs_metadata.json")

        search_engine = SemanticSearchEngine(
            corpus_embeddings_path=corpus_embeddings_path,
            analysis_df_path=analysis_df_path,
            package_descr_path=package_descr_path,
            device="cpu",  # Or "cuda" if available
        )
        logger.info("SemanticSearchEngine initialized successfully.")
    except Exception as e:
        logger.error(f"Failed to initialize SemanticSearchEngine: {e}")
        raise RuntimeError("Search engine initialization failed") from e


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
    logger.info(f"Response: {json.dumps(json_response, indent=2)}")
    return json_response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)