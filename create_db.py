from database import Base, engine

print('Creating database.....')
# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)