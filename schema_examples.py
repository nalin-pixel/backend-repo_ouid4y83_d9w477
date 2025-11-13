from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: str
    avatar_url: Optional[str] = None
    created_at: Optional[datetime] = None

class Post(BaseModel):
    id: Optional[str] = None
    title: str
    content: str
    tags: List[str] = []
    created_at: Optional[datetime] = None

class Task(BaseModel):
    id: Optional[str] = None
    title: str
    done: bool = False
    created_at: Optional[datetime] = None
