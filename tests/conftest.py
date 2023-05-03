from typing import Generator

import pytest
from fastapi.testclient import TestClient

from app.database import SessionLocal
from app.main import app


# This fixture returns a SessionLocal instance that is used to create a
# database session
@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


# This fixture returns a TestClient instance that is used to make requests
# to the application.
@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
