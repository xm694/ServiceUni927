#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 21:25:14 2023

@author: xiaomingmo
"""

from fastapi import FastAPI, Path, Query, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List, Annotated

import crud, models, schemas
from database import SessionLocal, engine

    
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

#user registration
@app.post("/register/",  response_model= schemas.user)
async def create_user(user:schemas.UserCreate, db:db_dependency):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registrered")
    return crud.create_user(db=db, user=user)

@app.get("/user/{user_id}", response_model=schemas.user)
async def read_user(user_id:str, db:db_dependency):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
        
#user apply for parking permit
@app.post("/user/{user_id}/apply_parking/", response_model= schemas.parking)
async def create_parking(owner_id:str, parking:schemas.ParkingCreate, db:db_dependency):
    return crud.create_parking(db=db, parking=parking, user_id=owner_id)

@app.get("/user/{user_id}/parking_records/", response_model= schemas.parking)
async def read_parking_application(owner_id:str, db:db_dependency):
    return crud.get_parking(db=db, user_id=owner_id)

#user apply for student card
@app.post("/user/{user_id}/stud_card/", response_model=schemas.card)
async def create_card(user_id:str, card: schemas.CardCreate, db:db_dependency):
    return crud.create_card(db=db, card=card, user_id=user_id)

@app.get("/user/{user_id}/card_records/", response_model=schemas.card)
async def read_card_records(user_id:str, db:db_dependency):
    return crud.get_card(db=db, user_id=user_id)