FROM ollama/ollama

# Install curl
RUN apt-get update && apt-get install -y curl

# Copy and allow execution of the entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
