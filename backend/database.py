from sqlite3 import Connection as SQLite3Connection
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

import os
load_dotenv()

class Base(DeclarativeBase):
    pass
engine = create_engine(os.getenv("DATABASE_URL"))

SessionLocal = sessionmaker(autocommit = False,bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
