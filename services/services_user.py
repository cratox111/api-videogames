from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from schemas.schemas_user import UserResponse
from repositories.repository_user import repositorie_get_user_by_mail, repositorie_create_user, repositorie_get_user_by_id, repositorie_get_users, repositorie_user_delete
from utils.security import hash_password
from utils.type_definition import ReturnMessage


def services_user_get(id: str, db: Session) -> UserResponse:
    user = repositorie_get_user_by_id(db=db, id=id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User no existe"
        )

    return UserResponse(
        id=user.id, 
        name=user.name,
        email=user.email,
        videogames=user.videogames
    )


def services_users_get(db: Session) -> list:
    users = repositorie_get_users(db=db)

    users_list = []
    for u in users:
        u = UserResponse(
            id=str(u.id), 
            name=u.name, 
            email=u.email, 
            videogames=u.videogames
        )
        
        users_list.append(u)

    return users_list


def services_user_create(name: str, email: str, password: str, db: Session) -> ReturnMessage:
    if repositorie_get_user_by_mail(db=db, email=email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El email ya existe"
        )
    
    password_hash = hash_password(password=password)

    repositorie_create_user(db=db, name=name, email=email, password=password_hash)

    return {"msg": "User creado"}


def services_delete_user(id: str, db: Session) -> ReturnMessage:
    user = repositorie_user_delete(db=db, id=id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User no existe"
        )

    return {'msg': 'User eliminado correctamente'}


def services_response_user(id: str, db: Session) -> UserResponse:
    user = repositorie_get_user_by_id(db=db, id=id)

    return UserResponse.model_validate(user)