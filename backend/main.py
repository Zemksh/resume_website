from fastapi import FastAPI
from .database import engine
from .database import get_db
from . import models
from .routes import notes, user


models.Base.metadata.create_all(bind=engine)
app = FastAPI()



app.include_router(notes.router)
app.include_router(user.router)
@app.get("/")
async def read_root():
    return {"Hello": "World"}