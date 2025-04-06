import requests
import json

def get_embedding(text: str, model: str = "nomic-embed-text") -> list:
    url = "http://localhost:11434/api/embeddings"
    headers = {"Content-Type": "application/json"}
    data = {"model": model, "prompt": text}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code != 200:
        raise RuntimeError(f"Embedding generation failed: {response.text}")

    result = response.json()
    return result["embedding"]
