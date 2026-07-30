from jose import jwt
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from repositories.repository_user import repositorie_get_user_by_mail
from utils.security import crypt, create_payload_token, SECRET, decode_token
from schemas.schemas_user import UserDB


oauth = OAuth2PasswordBearer(tokenUrl='/auth/login')


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
