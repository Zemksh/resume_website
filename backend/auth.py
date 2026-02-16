from datetime import datetime, timedelta
from jose import jwt, JWTerror
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from . import schema
from .config import SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"])
ouath2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")

def hash_password(password: str)-> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hash_password: str)-> bool:
    return pwd_context.verify(plain_password,hash_password)

def create_access_token(user_id: int) -> str:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub":str(user_id),expire}
    return jwt.encode(payload, SECRET_KEY, algorithm = ALGORITHM)

def verify_token(token: str) -> int:
    payload = jwt.decode(token, SECRET_KEY, algorithm = [ALGORITHM])
    user_id: str = payload.get("sub")
    if user_id is None:
        raise ValueError("Invalid token")
    return int(user_id)
