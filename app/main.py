from fastapi import FastAPI

from app.api.routes.health import router as health_router

app = FastAPI(
    title="DocuMind",
    description="Production Agentic RAG Platform",
    version="0.1.0",
)

app.include_router(health_router)


@app.get("/")
def root():
    return {"message": "Welcome to DocuMind API"}