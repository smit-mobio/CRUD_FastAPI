from datetime import datetime
from pydantic import BaseModel

class Items(BaseModel):
    name:str   
    price:int
    on_offer:bool
    created_on:datetime
    updated_on:datetime
    
    class Config:
        orm_mode = True