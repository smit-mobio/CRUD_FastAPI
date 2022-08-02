from __future__ import annotations

from datetime import datetime

import uvicorn
from fastapi import FastAPI
from fastapi import status
from fastapi_sqlalchemy import db

import models
from database import SessionLocal
from schema import Items

app = FastAPI()

db = SessionLocal()


@app.post('/items', response_model=Items, status_code=status.HTTP_201_CREATED)
def create_an_item(item: Items):
    new_item = models.Items(name=item.name, price=item.price, on_offer=item.on_offer,
                            created_on=datetime.now(), updated_on=datetime.now())
    db.add(new_item)
    db.commit()
    return new_item


@app.get('/items', response_model=list[Items], status_code=status.HTTP_200_OK)
def get_all_items():
    items = db.query(models.Items).all()
    return items


@app.get('/items/{id}')
def get_item(id: int):
    item = db.query(models.Items).filter_by(id=id).first()
    if not item:
        return {'message': 'Item not exists!'}
    return item


@app.patch('/items/{id}', status_code=status.HTTP_200_OK)
def update_item_partially(id: int, item: Items):
    item_to_update = db.query(models.Items).filter_by(id=id).first()
    if not item_to_update:
        return {'message': "Item you are looking for isn't exists!"}
    item_to_update.name = item.name
    item_to_update.updated_on = datetime.now()
    return {'message': 'Your item is successfully updated!'}


@app.put('/items/{id}', status_code=status.HTTP_200_OK)
def update_item_completly(id: int, item: Items):
    item_to_update = db.query(models.Items).filter_by(id=id).first()
    if not item_to_update:
        return {'message': "Item you are looking for isn't exists!"}
    item_to_update.name = item.name
    item_to_update.price = item.price
    item_to_update.on_offer = item.on_offer
    item_to_update.updated_on = datetime.now()
    return {'message': 'Your item is successfully updated!'}


@app.delete('/items')
def remove_all_items():
    items = models.Items.__table__.delete()
    db.execute(items)
    db.commit()
    return {'message': 'All items has been removed successfully!'}


@app.delete('/items/{id}')
def remove_an_item(id: int):
    item_to_remove = db.query(models.Items).filter_by(id=id).first()
    if not item_to_remove:
        return {'message': "Item you are looking for isn't exists!"}
    db.delete(item_to_remove)
    db.commit()
    return {'message': 'Your items has been removed successfully!'}


if __name__ == '__main__':
    uvicorn.run(app)
