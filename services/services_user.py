from fastapi import HTTPException, status

from repositories.repositorie_user import repositorie_get_user_by_mail, repositorie_create_user, repositorie_get_user_by_id, repositorie_get_users, repositorie_user_delete
from database.client import SessionLocal

db = SessionLocal()

def serveices_user_get(id: str):
    user = repositorie_get_user_by_id(db=db, id=id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User no existe"
        )

    return user


def serveices_users_get():
    users = repositorie_get_users(db=db)

    return users


def services_user_create(name: str, email: str, password: str):
    if repositorie_get_user_by_mail(db=db, email=email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El email ya existe"
        )
    
    repositorie_create_user(db=db, name=name, email=email, password=password)

    return {"msg": "User creado"}


def serveices_delete_user(id: str):
    user = repositorie_user_delete(db=db, id=id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User no existe"
        )

    return user