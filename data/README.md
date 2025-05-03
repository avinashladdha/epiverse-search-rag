# Azurite with Data Initialization

This setup provides a Dockerized environment for running Azurite (a local Azure Storage emulator) and initializing it with data from the local `data` folder. The `Dockerfile` and `init_azurite_data.sh` script work together to achieve this.

## Overview

- **Base Image**: Uses a minimal Debian-based image (`debian:stable-slim`).
- **Azurite Installation**: Azurite is installed via `npm` (Node.js package manager).
- **Azure CLI**: Installed in the container to interact with Azurite using the `az` command.
- **Initialization Script**: Copies all files from the local `data` folder into Azurite Blob Storage during container startup.

## Components

### 1. **Dockerfile**
- **Base Image**: Uses `debian:stable-slim` for a lightweight container.
- **Dependencies Installed**:
  - `curl`, `apt-transport-https`, `gnupg`, and other tools for installing Azure CLI.
  - `nodejs` and `npm` for installing Azurite.
- **Azurite Installation**: Installs Azurite globally using `npm install -g azurite`.
- **Initialization Script**: Copies the `init_azurite_data.sh` script into the container and makes it executable.
- **Exposed Ports**:
  - `10000`: Blob service
  - `10001`: Queue service
  - `10002`: Table service

### 2. **Initialization Script (`init_azurite_data.sh`)**
- **Starts Azurite**: Runs Azurite in the background.
- **Creates a Blob Container**: Creates a container named `data` in Azurite.
- **Uploads Files**: Iterates through all files in the `/data` directory and uploads them to the `data` container in Azurite Blob Storage.
- **Keeps Azurite Running**: Ensures the Azurite process continues running after initialization.

## How to Use

### 1. Build the Docker Image
Run the following command to build the Docker image:
```bash
docker build -t azurite-with-data .
```

### 2. Run the Container
Start the container with:
```bash
docker run -p 10000:10000 -p 10001:10001 -p 10002:10002 azurite-with-data
```

### 3. Verify the Setup
- Use the Azure CLI or Azurite's API to verify that the files have been uploaded to the `data` container in Azurite Blob Storage.
- Example Azure CLI command to list blobs:
  ```bash
  az storage blob list --container-name data --connection-string "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
  ```

## Notes
- Ensure the `data` folder contains the files you want to upload to Azurite before building the Docker image.
- The container will keep Azurite running after the initialization process.

## Example Use Case
This setup is useful for local development and testing of applications that interact with Azure Blob Storage. It allows you to emulate Azure Storage locally and prepopulate it with test data.
To upload any custom files to azurite, simply upload them to your `data` folder before running the container.