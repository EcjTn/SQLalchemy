from fastapi import FastAPI, Path, HTTPException, Depends, Query
from fastapi.responses import JSONResponse
from typing import List, Optional, Annotated
from pydantic import BaseModel
from sqlmodel import Session
from sqlalchemy.orm import Session as SQLAlchemySession
import models
from database import engine, SessionLocal
from schemas import UserCreate
from schemas import VipCreate

# FastAPI Setup
app = FastAPI(docs_url=None, redoc_url=None)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_session = Depends(get_db)

@app.post("/user/reg", status_code=201)
async def reg_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = models.PlayerBase(username=user.username, password=user.password)
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Username already exists")


    return new_user
    
@app.get("/users/all", status_code=200)
async def users_all(db: Session = Depends(get_db)):
    users = db.query(models.PlayerBase).all()
    return users



@app.get('/')
async def root():
    raise HTTPException(
        status_code=200,
        detail="Main page."
    )
