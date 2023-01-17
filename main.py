from fastapi import FastAPI, HTTPException, status
from database import get_database
from serializer import Planes, User
from pymongo import errors

app = FastAPI()

dbname = get_database()
collection_name = dbname["users"]
collection_name2 = dbname["fav_planes"]


@app.post("/plan_id/")
async def fav_plan(planes: Planes):
    collection_name2.insert_one(dict(planes))


@app.post('/signup')
def signup(user: User):
    try:
        collection_name.insert_one(dict(user))
        return {"New user created successfully"}
    except errors.DuplicateKeyError:
        return ("Duplicate key error:", user.email, "already exists in the collection")
