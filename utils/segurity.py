from dotenv import load_dotenv
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
import os

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

def decode_token(token: str):
    payload = jwt.decode(
        token,
        SECRET,
        algorithms=["HS256"]
    )

    return payload