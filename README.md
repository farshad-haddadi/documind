# DocuMind

DocuMind is a document management API built with FastAPI, PostgreSQL, and Docker. The project provides a foundation for document storage, metadata management, and retrieval through a RESTful API.

---

## Overview

The application exposes document management endpoints through FastAPI and persists document metadata in PostgreSQL. The entire stack is containerized with Docker and deployed on AWS EC2.

---

## Architecture

![Architecture](docs/images/architecture.png)

---

## Features

- FastAPI REST API
- PostgreSQL persistence layer
- SQLAlchemy ORM
- Alembic database migrations
- Dockerized deployment
- OpenAPI / Swagger documentation
- AWS EC2 deployment
- Health monitoring endpoint

---

## Technology Stack

| Component | Technology |
|------------|------------|
| Backend | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| API Documentation | Swagger / OpenAPI |
| Containerization | Docker |
| Orchestration | Docker Compose |
| Cloud Platform | AWS EC2 |

---

## API Documentation

Interactive API documentation is available at:

http://52.14.237.47:8001/docs

Health endpoint:

http://52.14.237.47:8001/health

---

## API Endpoints

| Method | Endpoint | Description |
|----------|----------|-------------|
| GET | /health | Service health check |
| GET | /documents | Retrieve all documents |
| GET | /documents/{document_id} | Retrieve a document |
| POST | /documents | Create a document |
| DELETE | /documents/{document_id} | Delete a document |

---

## Screenshots

### Swagger UI

![Swagger UI](docs/images/swagger-ui.png)

### AWS Deployment

![AWS Deployment](docs/images/aws-deployment.png)

### Document API

![Document API](docs/images/document-api.png)

---

## Local Development

### Clone Repository

```bash
git clone https://github.com/farshad-haddadi/documind.git
cd documind
```

### Configure Environment

Create a `.env` file:

```env
APP_NAME=DocuMind
APP_ENV=local
APP_VERSION=0.1.0

DATABASE_URL=postgresql+psycopg://documind:documind@postgres:5432/documind

EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
RERANKER_MODEL=cross-encoder/ms-marco-MiniLM-L-6-v2

FAISS_INDEX_PATH=data/indexes/documind.faiss

OPENAI_API_KEY=YOUR_API_KEY
OPENAI_MODEL=gpt-4.1-mini
```

### Start Services

```bash
docker-compose up -d
```

### Run Database Migrations

```bash
docker-compose exec api alembic upgrade head
```

---

## Deployment

The application is deployed on AWS EC2 using Docker Compose.

To verify the deployment:

```bash
curl http://localhost:8001/health
```

Expected response:

```json
{
  "status": "healthy",
  "service": "DocuMind",
  "version": "0.1.0",
  "environment": "local"
}
```

---

## Repository Structure

```text
documind/
├── .github/
│   └── workflows/
│       └── ci.yml
├── alembic/
├── app/
├── data/
├── docs/
│   └── images/
├── tests/
├── .env.example
├── .gitignore
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Author

**Farshad Haddadi**

GitHub: https://github.com/farshad-haddadi

LinkedIn: https://www.linkedin.com/in/farshad-haddadi-b932a7346