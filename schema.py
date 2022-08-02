from datetime import datetime
from pydantic import BaseModel

class Items(BaseModel):
    id:int
    name:str   
    price:int
    on_offer:bool
    created_on:datetime
    updated_on:datetime
    
    class Config:
        orm_mode = True