import logging
import os
import io  
import tensor
from calculate_embeddings import fetch_docs_and_embed
import azure.functions as func
from azure.storage.blob import BlobServiceClient

# --- Main Execution ---
def main(mytimer: func.TimerRequest) -> None:
    # Get environment variable
    connection_str = os.getenv("AzureWebJobsStorage")

    if not connection_str:
        logging.error("AzureWebJobsStorage environment variable is not set or empty!")
        raise ValueError("AzureWebJobsStorage is required but not provided.")

    logging.info(f"Using AzureWebJobsStorage: {connection_str}")

    blob_service_client = BlobServiceClient.from_connection_string(connection_str)
    container_name = "data"
    blob_csv = "analysis_df.csv"
    blob_pth = "corpus_embeddings.pth"

    # Ensure container exists
    container_client = blob_service_client.get_container_client(container_name)
    try:
        container_client.create_container()
    except Exception:
        pass  # It's okay if it already exists

    analysis_df, corpus_embeddings = fetch_docs_and_embed()

    # Upload blob
    blob_csv_client = container_client.get_blob_client(blob_csv)
    blob_csv_client.upload_blob(analysis_df.to_csv(index=False).encode('utf-8'), overwrite=True)

    blob_pth_client = container_client.get_blob_client(blob_pth)

    # Serialize tensor to a BytesIO object
    buffer = io.BytesIO()
    torch.save(corpus_embeddings, buffer)
    buffer.seek(0)  # Reset the buffer position to the beginning

    # Upload the buffer to Azure Blob Storage
    blob_pth_client.upload_blob(buffer, overwrite=True)