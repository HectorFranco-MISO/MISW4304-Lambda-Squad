import os
from unittest.mock import MagicMock

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

if os.getenv("TESTING") != "true":
    DB_USER = os.getenv('RDS_USERNAME')
    DB_PASSWORD = os.getenv('RDS_PASSWORD')
    DB_HOST = os.getenv('RDS_HOSTNAME')
    DB_PORT = os.getenv('RDS_PORT')
    DB_NAME = os.getenv('RDS_DB_NAME')

    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    engine = create_engine(
        DATABASE_URL,
        pool_size=20,
        max_overflow=30,
        pool_timeout=60,
        pool_recycle=1800
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
else:
    engine = MagicMock()
    SessionLocal = MagicMock()

Base = declarative_base()
