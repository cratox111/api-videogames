from passlib.context import CryptContext
from jose import jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from repositories.repositorie_user import repositorie_get_user_by_mail
from schemas.schemas_user import UserDB

load_dotenv()

oauth = OAuth2PasswordBearer(tokenUrl='/auth/login')

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

def decode_token(token: str):
    payload = jwt.decode(
        token,
        SECRET,
        algorithms=["HS256"]
    )

    return payload



def service_login(email: str, password: str, db: Session):
    user = repositorie_get_user_by_mail(
        db=db,
        email=email
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Email incorrecto"
        )

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



def get_current_user(token: str, db: Session):
    user = decode_token(token)
    return user['sub']