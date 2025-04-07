#!/bin/sh

# Start ollama in the background
ollama serve &

# Wait for the server to be ready
until curl -s http://localhost:11434 > /dev/null; do
  echo "Waiting for Ollama to start..."
  sleep 1
done

# Pull required models
ollama pull llama3
ollama pull nomic-embed-text

# Bring Ollama to foreground
tail -f /dev/null

