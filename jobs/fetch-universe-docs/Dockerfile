FROM mcr.microsoft.com/azure-functions/base:4

# Install R
RUN apt-get update && apt-get install -y r-base libcurl4-openssl-dev

RUN Rscript -e 'install.packages("pak")'

RUN Rscript -e 'pak::pak("epiverse-connect/epiverse-scraper")'

