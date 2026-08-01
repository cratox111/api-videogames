from pydantic import BaseModel, ConfigDict
from typing import Optional
from schemas.schemas_videogames import VideogameResponse


class UserForm(BaseModel):
    name: str
    email: str
    password: str


class UserDB(BaseModel):
    id: str
    name: str
    email: str


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str
    videogames: list[VideogameResponse]


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None