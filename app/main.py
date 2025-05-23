import os

from fastapi import FastAPI
from app.api.v1.router import api_router
from app.db import Base, engine

app = FastAPI(
    title="AWS Beanstalk - Lambda Squad",
    version="1.0.0"
)

app.include_router(api_router)

if os.getenv("TESTING") != "true":
    Base.metadata.create_all(bind=engine)
