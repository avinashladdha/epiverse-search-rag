FROM mcr.microsoft.com/azure-functions/python:4-python3.12

# Install R & relevant packages
RUN apt-get update && apt-get install -y r-base libcurl4-openssl-dev

RUN Rscript -e 'install.packages("pak")'

RUN Rscript -e 'pak::pak("epiverse-connect/epiverse-scraper")'

# Install relevant python libraries
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Copy function app files
ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY . /home/site/wwwroot
