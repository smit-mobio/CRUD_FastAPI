from datetime import datetime
from fastapi import FastAPI, status
from fastapi_sqlalchemy import db
import uvicorn
from database import SessionLocal
from schema import Items
import models

app = FastAPI()

db = SessionLocal()


@app.post('/items', response_model=Items, status_code=status.HTTP_201_CREATED)
def create_an_item(item:Items):
    new_item = models.Items(name = item.name, price = item.price, on_offer = item.on_offer, created_on = datetime.now(), updated_on = datetime.now())
    db.add(new_item)
    db.commit()
    return new_item

@app.get('/items', response_model=list[Items], status_code=status.HTTP_200_OK)
def get_all_items():
    items =  db.query(models.Items).all()
    return items

@app.get('/items/{id}')
def get_item(id:int):
    item =  db.query(models.Items).filter_by(id = id).first()
    if not item :
        return {'message': "Item not exists!"}
    return item

if __name__ == "__main__":
    uvicorn.run(app)