from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from services.services_user import services_user_create, serveices_user_get, serveices_users_get, serveices_delete_user
from schemas.schemas_user import UserForm
from database.client import get_db

route = APIRouter(prefix= "/user", tags=['User'])


@route.post('/')
async def route_user_create(data: UserForm, db: Session = Depends(get_db)):
    return services_user_create(
        name=data.name, 
        email=data.email, 
        password=data.password,
        db=db
    )


@route.get('/{id}')
async def route_user_get_id(id: str, db: Session = Depends(get_db)):
    return serveices_user_get(id=id, db=db)


@route.get('/')
async def route_user_get(db: Session = Depends(get_db)):
    return serveices_users_get(db=db)


@route.delete('/{id}')
async def route_user_delete(id: str, db: Session = Depends(get_db)):
    return serveices_delete_user(id=id, db=db)