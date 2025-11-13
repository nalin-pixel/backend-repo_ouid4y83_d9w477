from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from database import create_document, get_documents
from schemas import Product, Order, OrderItem

app = FastAPI(title="Jewelry Studio API")

# Allow frontend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProductCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    images: List[str] = []
    in_stock: bool = True

class OrderCreate(BaseModel):
    customer_name: str
    customer_email: str
    items: List[OrderItem]

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/test")
async def test_db():
    # simple query to verify connection
    docs = await get_documents("product", {}, limit=1)
    return {"db_ok": True, "sample": docs}

@app.get("/products")
async def list_products():
    products = await get_documents("product", {}, limit=100)
    return products

@app.post("/products")
async def create_product(payload: ProductCreate):
    data = payload.dict()
    saved = await create_document("product", data)
    return saved

@app.post("/orders")
async def create_order(payload: OrderCreate):
    # Calculate total based on provided items
    # For simplicity, expect frontend to send correct price or we can extend to fetch prices
    items_data = [item.dict() for item in payload.items]
    order_total = 0.0
    for item in items_data:
        # In a production app we'd fetch product and multiply price
        # Here we'll accept quantity only and leave pricing to future extension
        order_total += 0.0
    order = {
        "customer_name": payload.customer_name,
        "customer_email": payload.customer_email,
        "items": items_data,
        "total": order_total,
        "status": "pending",
    }
    saved = await create_document("order", order)
    return saved
