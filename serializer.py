from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext


class User(BaseModel):
    username: str
    email: EmailStr | None = None
    full_name: str | None = None
    password: str
    planes: list | None = None


class Planes(BaseModel):
    flight_iata: str
    users: list
