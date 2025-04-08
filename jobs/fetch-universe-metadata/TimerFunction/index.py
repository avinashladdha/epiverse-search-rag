import azure.functions as func
from azure.storage.blob import BlobServiceClient
import requests
import json
import os
import logging

def main(mytimer: func.TimerRequest):
    """
    Fetch metadata about packages from an R-universe repository.

    Args:
        universe (str): The name of the R-universe repository (default is "epiverse-connect").

    Returns:
        list: A list of dictionaries containing package metadata, including:
            - Package name
            - Title
            - Description
            - Logo URL
            - Website URL
            - Source repository URL
            - List of article URLs
    """

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


    universe = "epiverse-connect"
    url = f"https://{universe}.r-universe.dev/api/packages"
    headers = {"User-Agent": "epiverse-connect metadata collection script"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    package_metadata = response.json()

    processed_metadata = []
    for pkg in package_metadata:
        # We don't know if articles are hosted in a pkgdown website so we rely
        # on the rendered version hosted in our r-universe
        articles = [
            f"https://{universe}.r-universe.dev/articles/{pkg['Package']}/{vignette['filename']}"
            for vignette in pkg.get("_vignettes", [])
        ]

        url_list = [url.strip() for url in pkg.get("URL", "").split(',') if url.strip()]

        # First URL that doesn't look like a link to a GitHub repo
        docs_url = next((url for url in url_list if not url.startswith("https://github.com")), None)

        processed_metadata.append({
            "package": pkg.get("Package"),
            "title": pkg.get("Title"),
            "description": pkg.get("Description"),
            "logo": pkg.get("_pkglogo"),
            "website": docs_url,
            "source": pkg.get("RemoteUrl"),
            "articles": articles
        })
    #  store file locally if needed  
    with open("metadata.json", "w", encoding="utf-8") as f:
        json.dump(processed_metadata, f, indent = 4)
    
    # Upload blob
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(json.dumps(processed_metadata).encode('utf-8'), overwrite=True)

    # return processed_metadata
