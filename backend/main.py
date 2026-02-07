from fastapi import FastAPI
from sqlalchemy.orm import Session
from .schema import Notecreate
from .database import engine
from .database import get_db
from . import models
from fastapi.params import Depends
app = FastAPI()


models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/createitem")
async def create_item(new_note : Notecreate, db =  Depends(get_db)):
    newnote = models.Note(**new_note.model_dump())
    db.add(newnote)
    db.commit()
    db.refresh(newnote)
    return newnote

@app.get("/notes")
async def get_items(db:Session = Depends(get_db)):
    notes = db.query(models.Note).all()
    return notes

@app.put("/items/{item_id}")
async def update_item(item_id: int):
    return {"updated succesfully"}  

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"deleted succesfully"}