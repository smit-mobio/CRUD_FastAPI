from xml.etree.ElementTree import C14NWriterTarget
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from config import Config
app = FastAPI()

app.add_middleware(middleware_class=DBSessionMiddleware, db_url = Config.SQLALCHEMY_DATABASE_URL)