from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Annotated

from services.services_user import services_user_create, services_user_get, services_users_get, services_delete_user, services_response_user, services_upgrade_user
from services.services_auth import oauth, get_current_user
from schemas.schemas_user import UserForm, UserUpdate
from database.client import get_db

route = APIRouter(prefix= "/user", tags=['User'])



@route.get('/response')
async def route_user_reponse(token: Annotated[str, Depends(oauth)], db: Session = Depends(get_db)):
    return services_response_user(
        id=get_current_user(token=token, db=db),
        db=db
    )


@route.get('/{id}')
async def route_user_get_id(id: str, db: Session = Depends(get_db)):
    return services_user_get(id=id, db=db)


@route.get('/')
async def route_user_get(db: Session = Depends(get_db)):
    return services_users_get(db=db)


@route.post('/')
async def route_user_create(data: UserForm, db: Session = Depends(get_db)):
    return services_user_create(
        name=data.name, 
        email=data.email, 
        password=data.password,
        db=db
    )


@route.patch('/{id}')
async def route_user_upgrade(data: UserUpdate, token: Annotated[str, Depends(oauth)], db: Session = Depends(get_db)):
    return services_upgrade_user(
        id=get_current_user(token=token, db=db),
        name=data.name,
        email=data.email,
        password=data.password,
        db=db
    )


@route.delete('/{id}')
async def route_user_delete(id: str, db: Session = Depends(get_db)):
    return services_delete_user(id=id, db=db)


