FROM pytorch/torchserve

WORKDIR /jobs
COPY calculate_embedding.py .
COPY requirements.txt .
COPY logging_config.yaml .
COPY sources /sources/

RUN pip install -r requirements.txt
RUN pip install azure-functions azure-storage-blob azure-identity

CMD ["python3", "calculate_embedding.py"]







