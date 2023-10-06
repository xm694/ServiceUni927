#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 00:51:37 2023

@author: xiaomingmo
"""

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from database import Base
from sqlalchemy.orm import relationship
from random import randint

generated_user_id= String(randint(999, 9999999999))


#create tables want to save in database
class users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    '''
    #to do: student ID or staff ID, need to change to dynamic, 
    such as user_id = user_name[:3]+id
    '''
    user_id = Column(String, unique = True, default=generated_user_id)
    user_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    #user status as active or inactive user
    status = Column(String, default='active')
    #user could be undergrads, postgrads, staff
    role = Column(String)

    
class parking(Base):
    __tablename__ = 'parking'
    
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(String, ForeignKey('users.user_id'), unique = True, index=True)
    name = relationship("users", primaryjoin=(owner_id==users.user_id))
    plate_number = Column(String)
    #length will be 3 months, 6 months, 1 year
    permit_length = Column(String)
    start_date = Column(DateTime)
    '''
    #to do: a function to calculate the end time accordingly
    '''
    end_date = Column(DateTime)
    #process has 3 status: pending, approved, denied
    process = Column(String, default='pending')
    

class student_card(Base):
    __tablename__ = 'student_card'
    
    id = Column(Integer, primary_key=True, index=True)
    stud_id = Column(String, ForeignKey('users.user_id'), unique = True, index=True)
    name = relationship("users", primaryjoin=(stud_id==users.user_id))
    '''
    #to do: auto generate randic as card number
    '''
    card_number = Column(Integer, unique = True)
    delivery_method = Column(String)
    #status are pending, awaiting to pick up, posted, received
    status = Column(String, default='pending')
    