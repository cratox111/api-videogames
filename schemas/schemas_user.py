from pydantic import BaseModel, ConfigDict
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


class UserFormLogin(BaseModel):
    email: str
    password: str