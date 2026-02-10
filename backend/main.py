from fastapi import FastAPI
from .database import engine
from .database import get_db
from . import models
from .routes import notes
app = FastAPI()


models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(notes.router)