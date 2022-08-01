from database import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String


class Items(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    price = Column(Integer, nullable = False)
    on_offer = Column(Boolean, nullable = True)
    created_on = Column(DateTime, nullable = False)
    updated_on = Column(DateTime, nullable = True)
    