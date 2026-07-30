from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from schemas.schemas_user import UserResponse
from repositories.repository_user import repositorie_get_user_by_mail, repositorie_create_user, repositorie_get_user_by_id, repositorie_get_users, repositorie_user_delete
from utils.security import hash_password


def services_user_get(id: str, db: Session):
    user = repositorie_get_user_by_id(db=db, id=id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User no existe"
        )

    return user


def services_users_get(db: Session):
    users = repositorie_get_users(db=db)

    return users


def services_user_create(name: str, email: str, password: str, db: Session):
    if repositorie_get_user_by_mail(db=db, email=email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El email ya existe"
        )
    
    password_hash = hash_password(password=password)

    repositorie_create_user(db=db, name=name, email=email, password=password_hash)

    return {"msg": "User creado"}


def services_delete_user(id: str, db: Session):
    user = repositorie_user_delete(db=db, id=id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User no existe"
        )

    return user


def services_response_user(id: str, db: Session):
    user = repositorie_get_user_by_id(db=db, id=id)

    return UserResponse.model_validate(user)