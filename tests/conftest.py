import os
from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

# Configurar la variable de entorno antes de importar app
os.environ["TESTING"] = "true"

from app.main import app
from app.db import engine
from app.dependencies import get_db


@pytest.fixture(scope="function")
def mock_db():
    return MagicMock()


@pytest.fixture(scope="function", autouse=True)
def mock_engine(monkeypatch):
    mock_engine = MagicMock()
    monkeypatch.setattr(engine, "connect", mock_engine.connect)
    monkeypatch.setattr(engine, "dispose", mock_engine.dispose)
    return mock_engine


@pytest.fixture(scope="function")
def client(mock_db, mock_engine):
    def override_get_db():
        try:
            yield mock_db
        finally:
            mock_db.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()
