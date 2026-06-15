from fastapi import APIRouter

from services.services_user import services_user_create, serveices_user_get, serveices_users_get, serveices_delete_user
from schemas.schemas_user import UserForm

route = APIRouter(prefix= "/user", tags=['User'])


@route.post('/')
async def route_user_create(data: UserForm):
    return services_user_create(
        name=data.name, 
        email=data.email, 
        password=data.password
    )


@route.get('/{id}')
async def route_user_create(id: str):
    return serveices_user_get(id=id)


@route.get('/')
async def route_user_create():
    return serveices_users_get()


@route.delete('/{id}')
async def route_user_delete(id: str):
    return serveices_delete_user(id=id)