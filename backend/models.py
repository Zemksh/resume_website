from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer,primary_key=True, nullable=False)
    title = Column(String, nullable = False)
    content = Column(String)
    created_at = Column(TIMESTAMP(timezone= True), nullable = False, server_default = text('CURRENT_TIMESTAMP'))

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True, nullable = False)
    email = Column(String , nullable = False, unique = True)
    password = Column(String , nullable = False, unique = True)
    created_at = Column(TIMESTAMP(timezone= True), nullable = False, server_default = text('CURRENT_TIMESTAMP'))
