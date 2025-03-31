from fastapi import FastAPI
from app.api.v1.router import api_router
from app.db import Base, engine 

app = FastAPI(
    title="Mi Proyecto FastAPI",
    version="1.0.0"
)

app.include_router(api_router)

Base.metadata.create_all(bind=engine)
