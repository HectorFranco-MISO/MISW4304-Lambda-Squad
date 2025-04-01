from fastapi import APIRouter
from app.api.v1.endpoints import blacklist
from app.api.v1.endpoints import health

api_router = APIRouter()
api_router.include_router(blacklist.router, prefix="/blacklists", tags=["blacklists"])
api_router.include_router(health.router, prefix="/health", tags=["health"])
