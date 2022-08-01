from database import Base, engine
from models import ToDos

print('Creating database.....')

Base.metadata.create_all(engine)