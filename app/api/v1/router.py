from fastapi import APIRouter
from app.api.v1.endpoints import example
from app.api.v1.endpoints import blacklist

api_router = APIRouter()
api_router.include_router(example.router, prefix="/example", tags=["example"])
api_router.include_router(blacklist.router, prefix="/blacklists", tags=["blacklists"])
