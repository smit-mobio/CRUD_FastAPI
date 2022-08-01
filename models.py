from database import Base
from sqlalchemy import Column, Integer, String


class ToDos(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key = True)
    task = Column(String(100))