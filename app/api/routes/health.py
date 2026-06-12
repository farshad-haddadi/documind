from fastapi import APIRouter

from app.core.config import get_settings
from app.core.logging import get_logger

router = APIRouter(tags=["Health"])

logger = get_logger(__name__)


@router.get("/health")
def health_check():
    logger.info("Health check requested")

    settings = get_settings()

    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_env,
    }