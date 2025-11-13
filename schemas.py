from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# Each model corresponds to a MongoDB collection: class name lowercased

class Product(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    title: str
    description: Optional[str] = None
    price: float
    images: List[str] = []
    in_stock: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class OrderItem(BaseModel):
    product_id: str
    quantity: int = 1

class Order(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    customer_name: str
    customer_email: str
    items: List[OrderItem]
    total: float
    status: str = "pending"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
