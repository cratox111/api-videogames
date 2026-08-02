from fastapi import HTTPException, status
from dotenv import load_dotenv
from datetime import datetime, timedelta
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from jose import jwt, JWTError, ExpiredSignatureError
import os

from repositories.repository_user import repositorie_get_user_by_id

load_dotenv()

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

def validate_token(token: str, db: Session):
    try: 
        payload = jwt.decode(
            token,
            SECRET,
            algorithms=["HS256"]
        )

    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='El token a expirado'
        )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
    
    iss = payload.get('iss')
    sub = payload.get('sub')
    

    if iss != ISS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token inválido'
        )
    
    
    if not repositorie_get_user_by_id(db=db, id=sub):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='SUB invalido'
        )
    

    return payload
