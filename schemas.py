from pydantic import BaseModel
from datetime import datetime

class AdvertisementCreate(BaseModel):
    title: str
    description: str
    price: float
    author: str

class AdvertisementUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None