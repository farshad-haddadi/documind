# DocuMind

An Agentic Conversational RAG (Retrieval-Augmented Generation) platform built with FastAPI, PostgreSQL, Docker, FAISS, and OpenAI.

DocuMind allows users to upload documents, retrieve relevant information using semantic search, and interact with documents through natural language conversations.

---

## Live Demo

### Swagger UI

http://52.14.237.47:8001/docs

### Health Check

http://52.14.237.47:8001/health

---

## Screenshots

### Swagger API Documentation

![Swagger UI](docs/images/swagger-ui.png)

### System Architecture

![Architecture](docs/images/architecture.png)

---

## Features

- Document Upload API
- Conversational RAG Pipeline
- Semantic Search
- Vector Similarity Search with FAISS
- PostgreSQL Persistence
- OpenAI LLM Integration
- Dockerized Deployment
- AWS EC2 Hosting
- RESTful APIs
- Health Monitoring Endpoint
- Automated Testing with Pytest

---

## Architecture

```text
User
  │
  ▼
FastAPI
  │
  ├── Document Upload
  ├── Query API
  ├── Chat API
  │
  ▼
RAG Pipeline
  │
  ├── Chunking
  ├── Embedding Generation
  ├── Vector Search (FAISS)
  ├── Context Retrieval
  │
  ▼
OpenAI LLM
  │
  ▼
Response Generation
```

A visual architecture diagram can be found below:

![Architecture](docs/images/architecture.png)

---

## Tech Stack

### Backend

- FastAPI
- Python 3.11

### Database

- PostgreSQL

### AI / RAG

- OpenAI GPT-4.1 Mini
- FAISS
- Sentence Transformers
- BGE Embeddings
- Cross Encoder Reranking

### Infrastructure

- Docker
- Docker Compose
- AWS EC2

### Testing

- Pytest

---

## Project Structure

```text
documind/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── rag/
│   └── schemas/
│
├── tests/
│
├── docs/
│   └── images/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## API Endpoints

### Health

```http
GET /health
```

### Documents

```http
POST /documents/upload
```

### Query

```http
POST /query
```

### Chat

```http
POST /chat
```

---

## Local Development

### Clone Repository

```bash
git clone https://github.com/farshad-haddadi/documind.git
cd documind
```

### Create Environment File

```bash
cp .env.example .env
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
uvicorn app.main:app --reload
```

Application will be available at:

```text
http://localhost:8000
```

---

## Docker Deployment

### Build Containers

```bash
docker-compose up --build
```

### Run In Background

```bash
docker-compose up -d
```

### Verify Containers

```bash
docker ps
```

---

## AWS Deployment

DocuMind is deployed on AWS EC2 using Docker Compose.

### Infrastructure

- AWS EC2 (Ubuntu 24.04 LTS)
- Docker
- Docker Compose
- PostgreSQL Container
- FastAPI Container

### Public URLs

```text
http://52.14.237.47:8001/docs
```

```text
http://52.14.237.47:8001/health
```

---

## Testing

Run tests:

```bash
pytest
```

Example output:

```text
1 passed
```

---

## Future Improvements

- Multi-document collections
- User authentication
- Role-based access control
- Streaming responses
- Hybrid search
- Evaluation framework
- Observability and monitoring
- CI/CD pipeline with GitHub Actions
- HTTPS and custom domain
- Kubernetes deployment

---

## Lessons Learned

This project demonstrates:

- Building production-ready FastAPI services
- Designing Retrieval-Augmented Generation systems
- Vector databases and semantic search
- Docker containerization
- PostgreSQL integration
- Cloud deployment on AWS EC2
- API documentation with Swagger
- Software testing practices

---

## Author

**Farshad Haddadi**

GitHub:

https://github.com/farshad-haddadi

LinkedIn:

https://www.linkedin.com/in/farshad-haddadi-b932a7346

