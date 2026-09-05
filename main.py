#API Framework

from fastapi import FastAPI ,HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Tea(BaseModel):
    id : int
    name: str 
    origin: str

teas: list[Tea] = []

@app.get('/')
def read_root():
    return {"message": "welcome to tea house"}

@app.get('/teas') 
def get_teas():
    return teas 

@app.post('/teas')
def add_tea(tea : Tea):
    teas.append(tea)
    return tea

@app.put('/teas/{tea_id}')
def update_tea(tea_id: int, update_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = update_tea
            return update_tea
    return {"error": "tea not found"}

@app.delete('/teas/{tea_id}')
def delete_tea(tea_id : int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id :
            Deleted = teas.pop(index)
            return Deleted
    return {"error": "tea not found"}

@app.get("/item/{item_id}")
async def get_item(item_id: int):
    if item_id > 100:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Item not found"
        )
    return {"item_id": item_id}