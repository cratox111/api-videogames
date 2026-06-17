from passlib.context import CryptContext
from jose import jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
from fastapi import status, HTTPException


from database.client import SessionLocal
from repositories.repositorie_user import repositorie_get_user_by_mail
from schemas.schemas_user import UserDB

load_dotenv()

db = SessionLocal()

SECRET = os.getenv("SECRET")
ISS = os.getenv("ISS")

crypt = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

def create_payload_token(user_id: str):
    return {
        "sub": str(user_id),
        "exp": datetime.utcnow() + timedelta(minutes=30),
        "iss": ISS,
        "iat": datetime.utcnow(),
    }


def hash_password(password: str):
    h_password = crypt.hash(password)
    return h_password


def service_login(email: str, password: str):
    user_data = repositorie_get_user_by_mail(
        db=db,
        email=email
    )

    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Email incorrecto"
        )

    user = UserDB(**user_data)

    if not crypt.verify(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Contraseña incorrecta"
        )

    payload = create_payload_token(user.id)

    token = jwt.encode(
        payload,
        SECRET,
        algorithm="HS256"
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }