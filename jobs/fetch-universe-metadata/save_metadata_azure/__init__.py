import azure.functions as func
from azure.storage.blob import BlobServiceClient
from fetch_universe_metadata import fetch_universe_metadata
import json
import logging
import os

def main(mytimer: func.TimerRequest):

    # Get environment variable
    connection_str = os.getenv("AzureWebJobsStorage")

    if not connection_str:
        logging.error("AzureWebJobsStorage environment variable is not set or empty!")
        raise ValueError("AzureWebJobsStorage is required but not provided.")

    logging.info(f"Using AzureWebJobsStorage: {connection_str}")

    blob_service_client = BlobServiceClient.from_connection_string(connection_str)
    container_name = "metadata"
    blob_name = "metadata.json"

    # Ensure container exists
    container_client = blob_service_client.get_container_client(container_name)
    try:
        container_client.create_container()
    except Exception:
        pass  # It's okay if it already exists


    processed_metadata = fetch_universe_metadata("epiverse-trace")

    # Upload blob
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(json.dumps(processed_metadata).encode('utf-8'), overwrite=True)

