import requests
import logging
import json
from .config import OLLAMA_BASE_URL, OLLAMA_MODEL

logger = logging.getLogger(__name__)

def generate_answer(query: str, context_documents: list[str], model: str = OLLAMA_MODEL) -> str:
    """
    Generates an answer using Ollama based on the query and context documents.

    Args:
        query: The user's question.
        context_documents: A list of strings containing relevant context.
        model: The Ollama model to use.

    Returns:
        The generated answer string, or an error message if generation fails.
    """
    if not context_documents:
        return "No relevant documents found to generate an answer."

    # Construct the prompt
    context_str = "\n\n".join(context_documents)
    prompt = f"""You are a helpful assistant for the Epiverse-Connect project. 
Use the following context to answer the user's question. 
If the answer is not in the context, say you don't know.
Keep the answer concise and relevant.

Context:
{context_str}

Question: 
{query}

Answer:"""

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        url = f"{OLLAMA_BASE_URL}/api/generate"
        logger.info(f"Sending request to Ollama at {url} with model {model}")
        response = requests.post(url, json=payload, timeout=60) # 60s timeout
        response.raise_for_status()
        
        result = response.json()
        return result.get("response", "No response generated.")

    except requests.exceptions.RequestException as e:
        logger.error(f"Error communicating with Ollama: {e}")
        return "Error: Unable to generate answer. The local LLM service might be unavailable."
