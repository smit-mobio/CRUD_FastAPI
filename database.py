from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("postgresql://postgres:1605@localhost:5432/CRUD_FastAPI", echo= True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)