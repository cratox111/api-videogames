from pydantic import BaseModel

class UserForm(BaseModel):
    name: str
    email: str
    password: str