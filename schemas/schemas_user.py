from pydantic import BaseModel

class UserForm(BaseModel):
    name: str
    email: str
    password: str


class UserDB(BaseModel):
    id: str
    name: str
    email: str


class UserFormLogin(BaseModel):
    email: str
    password: str