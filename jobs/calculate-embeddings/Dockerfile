FROM mcr.microsoft.com/azure-functions/python:4-python3.12

COPY requirements.txt .
COPY logging_config.yaml .

RUN pip install -r requirements.txt
RUN pip install azure-functions azure-storage-blob azure-identity
# We do this at build time rather than runtime to save resources
RUN python -m nltk.downloader punkt_tab

# Install R & relevant packages
RUN apt-get update && apt-get install -y r-base libcurl4-openssl-dev
RUN Rscript -e 'install.packages("renv")'
COPY renv.lock renv.lock
RUN Rscript -e 'renv::restore()'

# Copied from https://github.com/Azure/azure-functions-core-tools?tab=readme-ov-file#debian-12
RUN apt-get update && apt-get install gpg wget -y && \
  wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | tee /usr/share/keyrings/microsoft-prod.gpg && \
  wget -q https://packages.microsoft.com/config/debian/12/prod.list && \
  mv prod.list /etc/apt/sources.list.d/microsoft-prod.list && \
  chown root:root /usr/share/keyrings/microsoft-prod.gpg && \
  chown root:root /etc/apt/sources.list.d/microsoft-prod.list && \
  apt-get update && apt-get install azure-functions-core-tools-4 -y && \
  apt-get update && apt-get install libicu-dev  -y

WORKDIR /home/site/wwwroot

# Copy function app files
COPY . /home/site/wwwroot/
ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true
