from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.core.config import get_settings
from app.core.logging import setup_logging, get_logger
from app.api.routes.documents import router as documents_router
from app.api.routes.query import router as query_router
from app.api.routes.chat import router as chat_router

setup_logging()

logger = get_logger(__name__)

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="Production Agentic RAG Platform",
    version=settings.app_version,
    debug=settings.debug,
)

app.include_router(health_router)
app.include_router(documents_router)
app.include_router(query_router)
app.include_router(chat_router)


@app.on_event("startup")
async def startup_event():
    logger.info("Starting DocuMind API")


@app.get("/")
def root():
    logger.info("Root endpoint called")

    return {
        "message": f"Welcome to {settings.app_name} API",
        "environment": settings.app_env,
    }