from sqlalchemy.orm import Session
from models.model_user import User

def repositorie_create_user(db: Session, name: str, email: str, password: str):
    db_user = User(name=name, email=email, password=password)

    db.add(db_user)
    db.commit()
    return "Creado"


def repositorie_get_user_by_mail(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def repositorie_get_user_by_id(db: Session, id: str):
    return db.query(User).filter(User.id == id).first()

def repositorie_get_users(db: Session):
    return db.query(User).all()


def repositorie_user_delete(db: Session, id: str):
    user = db.query(User).filter(User.id == id).first()
    db.delete(user)
    db.commit()

    return "Eliminado"
    