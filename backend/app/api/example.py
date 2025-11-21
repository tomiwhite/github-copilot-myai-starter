"""
Example API endpoints demonstrating basic CRUD operations.
Replace or extend this with your actual business logic.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, List

router = APIRouter()

# In-memory data store (replace with actual database in production)
items_db: Dict[int, Dict] = {}
next_id = 1


class Item(BaseModel):
    """Example item model."""
    name: str
    description: str
    price: float


class ItemResponse(BaseModel):
    """Item response with ID."""
    id: int
    name: str
    description: str
    price: float


@router.get("/items", response_model=List[ItemResponse])
async def get_items():
    """Get all items."""
    return [{"id": k, **v} for k, v in items_db.items()]


@router.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    """Get a specific item by ID."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **items_db[item_id]}


@router.post("/items", response_model=ItemResponse, status_code=201)
async def create_item(item: Item):
    """Create a new item."""
    global next_id
    item_id = next_id
    items_db[item_id] = item.model_dump()
    next_id += 1
    return {"id": item_id, **items_db[item_id]}


@router.put("/items/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: Item):
    """Update an existing item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item.model_dump()
    return {"id": item_id, **items_db[item_id]}


@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """Delete an item."""
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"message": "Item deleted successfully"}
