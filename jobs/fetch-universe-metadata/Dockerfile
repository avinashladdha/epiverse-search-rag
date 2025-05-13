FROM mcr.microsoft.com/azure-functions/python:4-python3.12

# to be added when volume is not mounted
# COPY . /home/site/wwwroot/
# RUN pip install -r /home/site/wwwroot/requirements.txt
RUN pip install azure-functions azure-storage-blob azure-identity

RUN apt-get update && \
    apt-get install -y curl apt-transport-https gnupg && \
    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ bionic main" > /etc/apt/sources.list.d/azure-cli.list && \
    apt-get update && \
    apt-get install -y azure-functions-core-tools-4 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /home/site/wwwroot

# Copy function app files
COPY . /home/site/wwwroot/
ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true
