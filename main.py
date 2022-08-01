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

if __name__ == "__main__":
    uvicorn.run(app)