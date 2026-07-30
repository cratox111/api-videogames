from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from services.services_auth import service_login
from database.client import get_db

route = APIRouter(prefix="/auth", tags=['Auth'])

@route.post('/login')
async def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return service_login(email=data.username, password=data.password, db=db)



