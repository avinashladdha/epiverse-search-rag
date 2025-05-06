FROM python:3.11-slim


WORKDIR /api

ENV USE_AZURE_STORAGE=true

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app into the container
COPY ./app ./app

EXPOSE 8000

# 
# RUN pip install -r requirements.txt
# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
