from fastapi import FastAPI, HTTPException, status, APIRouter,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schema
from fastapi.security import OAuth2PasswordBearer
from typing import List

router = APIRouter(
    prefix = "/user"
)


@router.get("/",response_model=List[schema.UserResponse])
async def get_all(db: Session = Depends(get_db)):
    query = db.query(models.User).all()
    return query

@router.post("/signup",response_model=schema.UserResponse)
async def signup(user : schema.UserCreate,db: Session = Depends(get_db)):
    newuser = models.User(**user.model_dump())
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser

@router.put("/{id}",response_model=schema.UserResponse)
async def update(id: int ,user : schema.UserCreate,db : Session =  Depends(get_db)):
    query = db.query(models.User).filter(models.User.id == id)
    selecteduser = query.first()
    if selecteduser is None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f"user with id: {id} nto found")
    query.update(user.model_dump())
    db.commit()
    return selecteduser

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete(id:int , db: Session = Depends(get_db)):
    query = db.query(models.User).filter(models.User.id == id)
    selecteduser = query.first()
    if selecteduser is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id : {id} is not found")
    query.delete()
    db.commit()
    return {"deleted succesfully"}
