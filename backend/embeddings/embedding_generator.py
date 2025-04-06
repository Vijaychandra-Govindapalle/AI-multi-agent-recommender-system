# backend/embeddings/embedding_generator.py

import requests
from database.db_manager import get_embedding_from_db, save_embedding_to_db

OLLAMA_URL = "http://localhost:11434/api/embeddings"
MODEL_NAME = "nomic-embed-text"

def get_embedding(text: str, entity_id: str, entity_type: str):
    cached = get_embedding_from_db(entity_id, entity_type)
    if cached:
        return cached

    response = requests.post(OLLAMA_URL, json={"model": MODEL_NAME, "prompt": text})
    if response.status_code == 200 and "embedding" in response.json():
        embedding = response.json()["embedding"]
        save_embedding_to_db(entity_id, entity_type, embedding)
        return embedding
    else:
        raise RuntimeError("Embedding generation failed")
