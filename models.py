from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

from database import Base


class Items(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Integer, nullable=False)
    on_offer = Column(Boolean, nullable=True)
    created_on = Column(DateTime, nullable=False)
    updated_on = Column(DateTime, nullable=True)
