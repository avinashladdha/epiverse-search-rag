# Epiverse search backend

This project implements a semantic search system using embeddings. It consists of two main parts: data acquisition and embedding generation, and a FastAPI endpoint for querying.

## 1. Data Acquisition and Embedding Generation

This part of the project handles scraping data, generating embeddings, and storing them for later use.

### Data Scraping

The data is scraped using a dedicated scraper.  You can find the scraper code in this repository: [[epiverse-scraper]([url](https://github.com/epiverse-connect/epiverse-scraper))].  This scraper is responsible for collecting the raw data that will be used for the search index.

### Embedding Generation

After scraping, the data is processed to generate embeddings.  This involves the following steps:

1. **Embedding Creation:**  We use multi-qa-MiniLM-L6-cos-v1 to generate embeddings for each data entry.
2. **Storage:** The generated embeddings, along with the original data, are stored as a .pth file (`corpus_embeddings.pth`) for efficient retrieval. 


## 2. FastAPI Endpoint for Search
This part of the project provides a FastAPI endpoint that handles search queries and returns the most relevant results.

![Alt text](epiverse search.drawio.png?raw=true "Flowchart")

