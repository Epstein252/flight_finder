from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, Body, HTTPException, status
import pymongo


def get_database():

    # Replace the uri string with your MongoDB deployment's connection string.
    conn_str = "mongodb+srv://epstein252:myfirstepstein252@cluster0.lrc4tzo.mongodb.net/?retryWrites=true&w=majority"

    # set a 5-second connection timeout
    client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
    return client['tal_flights']
