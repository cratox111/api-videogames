from sqlalchemy.orm import Session
from models.model_user import User

def repositorie_create_user(db: Session, name: str, email: str, password: str):
    db_user = User(name=name, email=email, password=password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return "Creado"


def repositorie_get_user_by_mail(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
    