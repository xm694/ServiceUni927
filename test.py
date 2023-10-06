#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 23:23:03 2023

@author: xiaomingmo
"""

from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None
    

app = FastAPI()

inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id:int = Path(None, description="The ID of the item")):
    return inventory[item_id]

@app.get('/get-by-name')
def get_item(name:str = Query(None, title="Name", description = "Name of the item")):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not found"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item ID not found.")
 
@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists."}
        raise HTTPException(status_code=400, detail= "Item ID already exists.")
    
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id:int, item:Item):
    if item_id not in inventory:
        return {"Error": "Item ID does not exists."}
    
    if item.name != None:
        inventory[item_id].name = item.name
        
    if item.price != None:
        inventory[item_id].price = item.price
    
    if item.brand != None:
        inventory[item_id].brand = item.brand
        
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description='The ID of item')):
    if item_id not in inventory:
        return {"error": "ID does not exists."}
    
    del inventory[item_id]
    return{"success": "item deleted."}