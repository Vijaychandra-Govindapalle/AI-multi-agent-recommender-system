# 🛍️ Hyper-Personalized Product Recommendation System

A multi-agent AI system delivering **hyper-personalized product recommendations** by understanding customer intent using a lightweight local LLM (TinyLlama), semantic embeddings, and multi-agent reasoning.

---

## ✨ Features

- 🤖 Multi-Agent Architecture (Customer Agent + Product Agent)
- 🧠 Intent Extraction with **TinyLlama** (LLM via Ollama)
- 📦 Product Matching using **Nomic Embeddings**
- 💬 Natural Language Input Support
- 🖼️ Clean Next.js frontend for displaying product recommendations
- 🐳 Fully Dockerized – Easy to run!

---

## 🧠 Tech Stack

| Layer         | Technology             |
|---------------|------------------------|
| Backend       | Python, FastAPI        |
| Frontend      | Next.js                |
| LLMs          | TinyLlama via Ollama   |
| Embeddings    | nomic-embed-text       |
| DB & Storage  | SQLite + CSV + Pandas  |
| Containerization | Docker, Docker Compose |

---

## 🔧 Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/) (usually bundled with Docker Desktop)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/product-recommender.git
cd product-recommender
```
### 2. Start the application with docker

```bash
docker-compose up --build
```
### 3. Set up ollama models

In a separate terminal
```bash
docker-compose exec -it ollama /bin/sh
```
```bash
ollama pull tinyllama
ollama pull nomic-embed-text
exit
```
### 4. Access the application at
http://localhost:3000

## Demo 

![AI_Demo-0](https://github.com/user-attachments/assets/3677f168-d97a-49fa-873a-2ca4018dd852)

![AI_Demo](https://github.com/user-attachments/assets/3b4034fc-c7e5-4181-a50a-810b3c0d6e78)

