from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
from datetime import datetime, timedelta
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from jose import jwt, JWTError, ExpiredSignatureError
import os
from typing import Annotated

from app.repositories.repository_user import repositorie_get_user_by_id
from app.schemas.schemas_user import UserResponse
from app.database.client import get_db

load_dotenv()

SECRET = os.getenv("SECRET")
ISS = os.getenv("ISS")
TIME_EXP = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

crypt = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

oauth = OAuth2PasswordBearer(tokenUrl='/auth/login')

def create_payload_token(user_id: str):
    return {
        "sub": str(user_id),
        "exp": datetime.utcnow() + timedelta(minutes=TIME_EXP),
        "iss": ISS,
        "iat": datetime.utcnow(),
    }


def hash_password(password: str):
    h_password = crypt.hash(password)
    return h_password

def validate_token(token: Annotated[str, Depends(oauth)], db: Session = Depends(get_db)):
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
    
    user = repositorie_get_user_by_id(db=db, id=sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token invalido'
        )
    

    return UserResponse(
        id=user.id,
        name=user.name,
        email=user.email,
        videogames=user.videogames
    )
