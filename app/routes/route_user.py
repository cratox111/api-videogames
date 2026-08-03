from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Annotated

from app.services.services_user import services_user_create, services_user_get, services_users_get, services_delete_user, services_response_user, services_upgrade_user
from app.schemas.schemas_user import UserForm, UserUpdate, UserResponse
from app.database.client import get_db
from app.utils.security import validate_token

route = APIRouter(prefix= "/user", tags=['User'])


@route.get('/response')
async def route_user_reponse(user_current: Annotated[UserResponse, Depends(validate_token)], db: Session = Depends(get_db)):
    return services_response_user(
        id=user_current.id,
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
async def route_user_upgrade(data: UserUpdate, user_current: Annotated[UserResponse, Depends(validate_token)], db: Session = Depends(get_db)):
    return services_upgrade_user(
        id=user_current.id,
        name=data.name,
        email=data.email,
        password=data.password,
        db=db,
        user_current=user_current
    )


@route.delete('/{id}')
async def route_user_delete(id: str, user_current: Annotated[UserResponse, Depends(validate_token)], db: Session = Depends(get_db)):
    return services_delete_user(
        id=id, 
        db=db,
        user_current=user_current
    )


