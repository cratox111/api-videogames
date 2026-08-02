from jose import jwt
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from repositories.repository_user import repositorie_get_user_by_mail
from utils.security import crypt, create_payload_token, SECRET
from utils.type_definition import TokenAcces


def service_login(email: str, password: str, db: Session) -> TokenAcces:
    user = repositorie_get_user_by_mail(
        db=db,
        email=email
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Credenciales incorrectas"
        )

    if not crypt.verify(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Credenciales incorrectas"
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
