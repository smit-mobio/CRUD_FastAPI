from __future__ import annotations

from database import Base
from database import engine

print('Creating database.....')
# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
