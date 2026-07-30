from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URI")


class Base(DeclarativeBase):
    pass


# Configura el Engine con la información necesaria para conectarse a la base de datos
engine = create_engine(
    DATABASE_URL,
    echo=False
)


# Fábrica encargada de crear nuevas sesiones de SQLAlchemy
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# Proporciona una sesión para cada petición y la cierra al finalizar
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
