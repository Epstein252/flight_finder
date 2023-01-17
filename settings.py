from fastapi.middleware.cors import CORSMiddleware
from main import app

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods= ["*"],
    allow_headers= ["*"]
    
)