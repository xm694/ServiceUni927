#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:54:13 2023

@author: xiaomingmo
"""

from pydantic import BaseModel
from datetime import date
from typing import Optional


#for the parking table
class ParkingBase(BaseModel):
    owner_id:str
    plate_number: str
    
class ParkingCreate(ParkingBase):
    permit_length: str

class parking(ParkingBase):
    id: int #case request id
    name: str
    process: str
    start_date: Optional[date] #here need to match with the datetime in models.py
    end_date: Optional[date]
    
    class Config:
        orm_mod = True
        

#for the student card table
class CardBase(BaseModel):
    stud_id: str
    name: str

class CardCreate(CardBase):
    delivery_method: str
    
class card(CardBase):
    card_number: int
    status: str
    
    class Config:
        orm_mod = True

        
#for the user table
class UserBase(BaseModel):
    user_name: str
    email: str
    role: str
    
class UserCreate(UserBase):
    password: str
    
class user(UserBase):
    user_id: str  
    status: str
    parkings: list[parking] = []
    stud_cards: list[card] = []
    
    class Config:
        orm_mod = True