from .models import Advertisement
from .schemas import AdvertisementCreate, AdvertisementUpdate
from datetime import datetime
import uuid

# Хранение объявлений в памяти
advertisements = {}


def create_advertisement(ad: AdvertisementCreate):
    ad_id = str(uuid.uuid4())
    created_at = datetime.now()
    advertisement = Advertisement(
        id=ad_id,
        title=ad.title,
        description=ad.description,
        price=ad.price,
        author=ad.author,
        created_at=created_at
    )
    advertisements[ad_id] = advertisement
    return advertisement


def update_advertisement(ad_id: str, ad: AdvertisementUpdate):
    if ad_id not in advertisements:
        return None

    advertisement = advertisements[ad_id]
    if ad.title:
        advertisement.title = ad.title
    if ad.description:
        advertisement.description = ad.description
    if ad.price:
        advertisement.price = ad.price

    return advertisement


def delete_advertisement(ad_id: str):
    if ad_id in advertisements:
        del advertisements[ad_id]
        return True
    return False


def get_advertisement(ad_id: str):
    return advertisements.get(ad_id)


def search_advertisements(title: str = None, author: str = None):
    results = []
    for ad in advertisements.values():
        if title and title.lower() not in ad.title.lower():
            continue
        if author and author.lower() not in ad.author.lower():
            continue
        results.append(ad)

    return results