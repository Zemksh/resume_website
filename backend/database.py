from sqlite3 import Connection as SQLite3Connection
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os
load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

if engine :
    print("Database engine created successfully.")