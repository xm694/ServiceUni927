#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 12:21:36 2023

@author: xiaomingmo
"""

from sqlalchemy.orm import Session
import models, schemas

#for user
#get single user
def get_user(db:Session, user_id: str):
    return db.query(models.users).filter(models.users.user_id == user_id).first()

def get_user_by_email(db:Session, email:str):
    return db.query(models.users).filter(models.users.email == email).first()

#get all users
def get_users(db:Session, skip: int=0, limit: int=100):
    return db.query(models.users).offset(skip).limit(limit).all()

def create_user(db:Session, user: schemas.UserCreate):
    '''
    to do: need to create user authentication mechanism for the password

    '''
    fake_hashed_password = user.password + 'notreallyhashed'
    db_user = models.users(user_name=user.user_name, email = user.email, role=user.role, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#for parking
#get parking permit application by user_id
def get_parking(db:Session, user_id:str):
    return db.query(models.parking).filter(models.parking.owner_id == user_id).all()

def create_parking(db:Session, parking:schemas.ParkingCreate, user_id:str):
    db_parking = models.parking(**parking.dict(), owner_id=user_id)
    db.add(db_parking)
    db.commit()
    db.refresh(db_parking)
    return db_parking

#for student card
def get_card(db:Session, user_id:str):
    return db.query(models.student_card).filter(models.student_card.user_id == user_id).first()

def create_card(db:Session, card:schemas.CardCreate, user_id:str):
    db_card = models.student_card(**card.dict(), stud_id=user_id)
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card