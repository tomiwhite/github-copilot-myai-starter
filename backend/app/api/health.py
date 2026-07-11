"""
Health check endpoints for monitoring and readiness probes.
"""
from fastapi import APIRouter
from datetime import datetime, timezone

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Basic health check endpoint.
    Returns 200 OK if the service is running.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@router.get("/ready")
async def readiness_check():
    """
    Readiness check endpoint.
    Returns 200 OK if the service is ready to handle requests.
    Can be extended to check database connections, external services, etc.
    """
    # Add checks for dependencies here (database, cache, etc.)
    return {
        "status": "ready",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
