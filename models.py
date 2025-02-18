from pydantic import BaseModel
from datetime import datetime

class Advertisement(BaseModel):
    id: str
    title: str
    description: str
    price: float
    author: str
    created_at: datetime