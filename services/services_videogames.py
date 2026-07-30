from fastapi import status, HTTPException, Depends

from repositories.repository_videogames import repositorie_create_game, repositorie_get_videogames, repositorie_get_videogames_by_id, repositorie_get_videogames_by_title, repositorie_videogame_delete
from sqlalchemy.orm import Session


def services_get_game_by_title(title: str, db: Session):
    game = repositorie_get_videogames_by_title(db=db, title=title)

    if not game:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="EL juego no existe"
        )
    
    return game


def services_get_game_by_id(id: str, db: Session):
    game = repositorie_get_videogames_by_id(db=db, id=id)

    if not game:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="EL juego no existe"
        )
    
    return game


def serveices_games_get(db: Session):
    games = repositorie_get_videogames(db=db)

    return games
    

def services_add_game(title: str, description: str, version: str, owner_id: str, url_download: str, db: Session):
    if repositorie_get_videogames_by_title(db=db, title=title):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="EL juego ya existe"
        )
    
    repositorie_create_game(db=db, title=title, description=description, version=version, owner_id=owner_id, url_download=url_download)

    return {"msg": "Juego añadido correctamente"}


def services_delete_game(id: str, db: Session):
    game = repositorie_get_videogames_by_id(db=db, id=id)

    if not game:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="EL juego no existe"
        )

    repositorie_videogame_delete(db=db, id=id)

    return {"msg": "Juego eliminado"}