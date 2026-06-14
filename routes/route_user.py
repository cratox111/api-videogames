from fastapi import APIRouter

from services.services_user import services_user_create
from schemas.schemas_user import UserForm

route = APIRouter(prefix= "/user", tags=['User'])


@route.post('/')
async def route_user_create(data: UserForm):
    return services_user_create(
        name=data.name, 
        email=data.email, 
        password=data.password
    )