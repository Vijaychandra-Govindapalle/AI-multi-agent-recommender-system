import requests
from database.db_manager import get_embedding_from_db, save_embedding_to_db

OLLAMA_URL = "http://172.17.0.1:11434/api/embeddings"
MODEL_NAME = "nomic-embed-text"

def get_embedding(text: str, entity_id: str, entity_type: str):
    cached = get_embedding_from_db(entity_id, entity_type)
    if cached:
        return cached

    if not text or not text.strip():
        raise ValueError(f"Empty text passed for embedding (Entity: {entity_id}, Type: {entity_type})")

    payload = {
        "model": MODEL_NAME,
        "prompt": text
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()

        if "embedding" not in data:
            raise RuntimeError(f"No embedding found in response: {data}")

        embedding = data["embedding"]
        save_embedding_to_db(entity_id, entity_type, embedding)
        return embedding

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Request failed: {e}")
    except ValueError as ve:
        raise RuntimeError(f"Invalid text input: {ve}")
    except Exception as e:
        raise RuntimeError(f"Embedding generation failed for entity {entity_id} of type {entity_type}: {e}")
