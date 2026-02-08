from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from .schema import Notecreate
from .database import engine
from .database import get_db
from . import models,schema
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

@app.get("/notes",response_model=schema.NoteResponse)
async def get_items(db:Session = Depends(get_db)):
    notes = db.query(models.Note).all()
    return notes

@app.get("/notes/{id}",response_model=schema.NoteResponse)
async def get_items(id:int, db:Session = Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id == id).first()
    return note

@app.put("/notes/{id}",response_model=schema.NoteResponse)
async def update_item(id: int, updated_note : schema.Notecreate, db: Session= Depends(get_db)):
    updnote_query= db.query(models.Note).filter(models.Note.id == id)
    updnote = updnote_query.first()
    if updnote is None:
        raise HTTPException(status_code=404, detail="Item not found")
    updnote_query.update(updated_note.model_dump(),synchronize_session=False)
    db.commit()
    return updnote_query.first()

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"deleted succesfully"}