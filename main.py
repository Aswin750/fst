from fastapi import FastAPI,Depends
from database import SessionLocal,engine
from sqlalchemy import text
import database_models
from sqlalchemy.orm import Session
from models import UserCreate

app=FastAPI()

database_models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def greet():
    return "Hi"


@app.get("/users")
def get_userdata(db:Session=Depends(get_db)):
    users=db.query(database_models.user).all()
    return users