from fastapi import FastAPI, Depends
from .database import engine
from .database import get_db
from . import models
from .routes import notes, user
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

app.include_router(notes.router)
app.include_router(user.router)
@app.get("/")
async def read_root():
    return {"Hello": "World"}