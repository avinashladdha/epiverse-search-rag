#!/bin/bash
# filepath: /home/bafnaprincy/epiverse/epiverse-search-backend/data/init.sh

# Start Azurite in the background
azurite --blobHost 0.0.0.0 --queueHost 0.0.0.0 --tableHost 0.0.0.0 &

# Wait for Azurite to start
sleep 5

# Set up Azurite connection string
AZURITE_CONNECTION_STRING="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;"

# Create a container in Azurite
echo "Creating container 'data'..."
az storage container create --name data --connection-string "$AZURITE_CONNECTION_STRING"

# Upload all files from the /data folder to Azurite
echo "Uploading files to Azurite Blob Storage..."
for file in /data/*; do
    if [ -f "$file" ]; then
        blob_name=$(basename "$file")
        az storage blob upload --container-name data --file "$file" --name "$blob_name" --connection-string "$AZURITE_CONNECTION_STRING"
        echo "Uploaded $blob_name to Azurite."
    fi
done

# Keep Azurite running
wait