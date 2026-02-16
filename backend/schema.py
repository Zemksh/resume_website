from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class Notecreate(BaseModel):
    title: str
    content: str

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email : EmailStr
    password : str

class UserResponse(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime
    class Config:
        from_attributes = True
        orm_mode = True
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    acess_token: str
    token_type: str

class TokenData(BaseModel):
    id: int |None = None
