from sqlalchemy.orm import Session
from app.models.model_videogames import Videogame



def repositorie_create_game(db: Session, title: str, description: str, version: str, owner_id: int, url_download: str):
    db_game = Videogame(
        title=title,
        description=description,
        version=version,
        owner_id=owner_id,
        url_download=url_download
    )

    db.add(db_game)
    db.commit()
    return "Creado"


def repositorie_get_videogames_by_title(db: Session, title: str):
    return db.query(Videogame).filter(Videogame.title == title).first()

def repositorie_get_videogames_by_id(db: Session, id: int):
    return db.query(Videogame).filter(Videogame.id == id).first()

def repositorie_get_videogames(db: Session):
    return db.query(Videogame).all()


def repositorie_videogame_delete(db: Session, id: int):
    db.query(Videogame).filter(Videogame.id == id).delete()
    db.commit()

    return "Eliminado"