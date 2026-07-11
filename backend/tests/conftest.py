"""
Pytest configuration and fixtures for backend tests.
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    return TestClient(app)


@pytest.fixture
def sample_item():
    """Create a sample item for testing."""
    return {
        "name": "Test Item",
        "description": "A test item for unit tests",
        "price": 99.99
    }
