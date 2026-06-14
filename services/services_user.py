from fastapi import HTTPException, status

from repositories.repositorie_user import repositorie_get_user_by_mail, repositorie_create_user
from database.client import SessionLocal

db = SessionLocal()

def services_user_create(name: str, email: str, password: str):
    if repositorie_get_user_by_mail(db=db, email=email):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="El email ya existe"
        )
    
    repositorie_create_user(db=db, name=name, email=email, password=password)

    return {"msg": "User creado"}