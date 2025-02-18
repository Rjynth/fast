from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid

app = FastAPI()


# Модель объявления
class Advertisement(BaseModel):
    id: str
    title: str
    description: str
    price: float
    author: str
    created_at: datetime


# Хранение объявлений в памяти
advertisements = {}


# Создание объявления
@app.post("/advertisement", response_model=Advertisement)
def create_advertisement(title: str, description: str, price: float, author: str):
    ad_id = str(uuid.uuid4())
    created_at = datetime.now()
    advertisement = Advertisement(
        id=ad_id,
        title=title,
        description=description,
        price=price,
        author=author,
        created_at=created_at
    )
    advertisements[ad_id] = advertisement
    return advertisement


# Обновление объявления
@app.patch("/advertisement/{advertisement_id}", response_model=Advertisement)
def update_advertisement(advertisement_id: str, title: Optional[str] = None, description: Optional[str] = None,
                         price: Optional[float] = None):
    if advertisement_id not in advertisements:
        raise HTTPException(status_code=404, detail="Advertisement not found")

    ad = advertisements[advertisement_id]
    if title:
        ad.title = title
    if description:
        ad.description = description
    if price:
        ad.price = price

    return ad


# Удаление объявления
@app.delete("/advertisement/{advertisement_id}")
def delete_advertisement(advertisement_id: str):
    if advertisement_id not in advertisements:
        raise HTTPException(status_code=404, detail="Advertisement not found")

    del advertisements[advertisement_id]
    return {"message": "Advertisement deleted"}


# Получение объявления по ID
@app.get("/advertisement/{advertisement_id}", response_model=Advertisement)
def get_advertisement(advertisement_id: str):
    if advertisement_id not in advertisements:
        raise HTTPException(status_code=404, detail="Advertisement not found")

    return advertisements[advertisement_id]


# Поиск объявлений по полям
@app.get("/advertisement", response_model=List[Advertisement])
def search_advertisements(title: Optional[str] = Query(None), author: Optional[str] = Query(None)):
    results = []
    for ad in advertisements.values():
        if title and title.lower() not in ad.title.lower():
            continue
        if author and author.lower() not in ad.author.lower():
            continue
        results.append(ad)

    return results