# 🧠 RAG-Based Q&A Support Bot (Python)

A **Retrieval Augmented Generation (RAG)** based Q&A support bot that answers user questions **only from a crawled website**.  
The project demonstrates the **complete RAG workflow** including crawling, chunking, embeddings, vector search, and answer generation via an API.

---

## ✨ Features

- 🌐 Crawl any website
- 🧹 Clean & chunk website content
- 🧠 Generate embeddings
- 📦 Store vectors using FAISS
- 🔍 Retrieve relevant context
- 🤖 Generate answers using LLM (RAG)
- 🚀 REST API using FastAPI
- 🧪 Testable via Postman or curl

---

## 🏗️ Architecture Diagram

```
Target Website
      │
      ▼
Web Crawler
      │
      ▼
Text Cleaning & Chunking
      │
      ▼
Embedding Model
      │
      ▼
Vector Database (FAISS)
      │
      ▼
Retriever (Top-K)
      │
      ▼
LLM Answer Generator
      │
      ▼
FastAPI Endpoint
```

---

## 📁 Project Structure

```
rag-support-bot/
│
├── app.py
├── crawler.py
├── text_processing.py
├── embeddings.py
├── vector_store.py
├── rag.py
├── config.py
├── requirements.txt
├── README.md
└── data/
```

---

## ⚙️ Tech Stack

- **Python 3.9+**
- **FastAPI**
- **FAISS**
- **Sentence Transformers**
- **BeautifulSoup**
- **OpenAI API**
- **Postman / curl**

---


## ⚙️ Installation

### 1️⃣ Clone Repository 

```bash
git clone https://github.com/rishekundey/rag-support-bot.git
cd rag-support-bot
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```
#### Activate:

#### Windows
```bash
venv\Scripts\activate
```

#### Mac / Linux
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variable

#### Windows
```bash
setx OPENAI_API_KEY "sk-xxxx"
```

#### Mac/Linux
```bash
export OPENAI_API_KEY="sk-xxxx"
```

---

## 🚀 Running the Pipeline

#### Update target website

#### Edit config.py → BASE_URL = "https://your-target-site.com"

#### ⚠️ These steps must be run once before starting the API

```bash
python crawler.py
python text_processing.py
python embeddings.py
python vector_store.py
```

---

## 🟢 Start API

```bash
uvicorn app:app --reload
```

---

## 🧪 Testing

### ✅ Health Check
```bash
curl http://127.0.0.1:8000/health
```

# 🤖 Ask a Question

### curl
```bash
curl -X POST http://127.0.0.1:8000/ask \
-H "Content-Type: application/json" \
-d '{"question":"What is this website about?"}'
```

### Postman
- Method: POST
- URL: http://127.0.0.1:8000/ask
- Params → Key: question and  Value: What is this website about?
- Body → raw → JSON (Optional)

---

