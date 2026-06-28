from http.client import HTTPException
from typing import List
from fastapi import FastAPI
from data_models.UserModel import UserCreate, UserGet
import uuid

app = FastAPI()
db=[]

@app.get("/")
def main():
    return {"Status": "OK"}

@app.post("/create-user", response_model=UserGet)
def create_user(data: UserCreate):

    data = data.model_dump()
    id = uuid.uuid4()
    data["id"]= id
    db.append(data)

    return data

@app.get('/get-users', response_model=List[UserGet])
def get_users():
    return db

@app.get('/get-user/{id}', response_model=UserGet)
def get_user(id:uuid.UUID):
    for user in db:
        if user["id"] == id:
            return user
    return HTTPException("User not found")

@app.delete("/delete-user/{id}")
def delete_user(id: uuid.UUID):
    for user in db:
        if user['id'] == id:
            db.remove(user)
    return {"Removed" : True}