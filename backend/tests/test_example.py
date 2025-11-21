"""
Tests for example CRUD endpoints.
"""
import pytest
from fastapi.testclient import TestClient


def test_get_items_empty(client: TestClient):
    """Test getting items when database is empty."""
    response = client.get("/api/v1/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_item(client: TestClient, sample_item):
    """Test creating a new item."""
    response = client.post("/api/v1/items", json=sample_item)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == sample_item["name"]
    assert data["description"] == sample_item["description"]
    assert data["price"] == sample_item["price"]
    assert "id" in data


def test_get_item(client: TestClient, sample_item):
    """Test getting a specific item."""
    # First create an item
    create_response = client.post("/api/v1/items", json=sample_item)
    item_id = create_response.json()["id"]
    
    # Then get it
    response = client.get(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == sample_item["name"]


def test_get_nonexistent_item(client: TestClient):
    """Test getting a non-existent item."""
    response = client.get("/api/v1/items/99999")
    assert response.status_code == 404


def test_update_item(client: TestClient, sample_item):
    """Test updating an existing item."""
    # Create an item
    create_response = client.post("/api/v1/items", json=sample_item)
    item_id = create_response.json()["id"]
    
    # Update it
    updated_data = {
        "name": "Updated Item",
        "description": "Updated description",
        "price": 149.99
    }
    response = client.put(f"/api/v1/items/{item_id}", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == updated_data["name"]
    assert data["price"] == updated_data["price"]


def test_delete_item(client: TestClient, sample_item):
    """Test deleting an item."""
    # Create an item
    create_response = client.post("/api/v1/items", json=sample_item)
    item_id = create_response.json()["id"]
    
    # Delete it
    response = client.delete(f"/api/v1/items/{item_id}")
    assert response.status_code == 200
    assert "message" in response.json()
    
    # Verify it's deleted
    get_response = client.get(f"/api/v1/items/{item_id}")
    assert get_response.status_code == 404


def test_delete_nonexistent_item(client: TestClient):
    """Test deleting a non-existent item."""
    response = client.delete("/api/v1/items/99999")
    assert response.status_code == 404
