from fastapi import status, HTTPException, Depends

from repositories.repository_videogames import repositorie_create_game, repositorie_get_videogames, repositorie_get_videogames_by_id, repositorie_get_videogames_by_title, repositorie_videogame_delete
from schemas.schemas_videogames import VideogameResponse
from sqlalchemy.orm import Session
from utils.type_definition import ReturnMessage


def services_get_game_by_title(title: str, db: Session) -> VideogameResponse:
    game = repositorie_get_videogames_by_title(db=db, title=title)

    if not game:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El juego no existe"
        )
    
    return VideogameResponse(
        id=game.id,
        title=game.title,
        description=game.description,
        version=game.version,
        created_at=game.created_at,
        likes_count=game.likes_count,
        url_download=game.url_download
    )


def services_get_game_by_id(id: str, db: Session) -> VideogameResponse:
    game = repositorie_get_videogames_by_id(db=db, id=id)

    if not game:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="EL juego no existe"
        )
    
    return VideogameResponse(
        id=game.id,
        title=game.title,
        description=game.description,
        version=game.version,
        created_at=game.created_at,
        likes_count=game.likes_count,
        url_download=game.url_download
    )


def services_games_get(db: Session) -> list:
    games = repositorie_get_videogames(db=db)

    games_list = []
    for g in games:
        g = VideogameResponse(
            id=g.id,
            title=g.title,
            description=g.description,
            version=g.version,
            created_at=g.created_at,
            likes_count=g.likes_count,
            url_download=g.url_download
        )
        
        games_list.append(g)

    return games_list
    

def services_add_game(title: str, description: str, version: str, owner_id: str, url_download: str, db: Session) -> ReturnMessage:
    if repositorie_get_videogames_by_title(db=db, title=title):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="EL juego ya existe"
        )
    
    repositorie_create_game(db=db, title=title, description=description, version=version, owner_id=owner_id, url_download=url_download)

    return {"msg": "Juego añadido correctamente"}


def services_upgrade_game(title: str, db: Session, new_title: str, description: str, version: str, url_download: str) -> ReturnMessage:
    current_game = repositorie_get_videogames_by_title(db=db, title=title)

    if new_title != "":
        current_game.title = new_title
    
    if description != "":
        current_game.description = description
    
    if version != "":
        current_game.version = version

    if url_download != "":
        current_game.url_download = url_download

    db.commit()
    db.refresh(current_game)

    return {'msg': 'Game actualizado'}


def services_delete_game(id: str, db: Session) -> ReturnMessage:
    game = repositorie_get_videogames_by_id(db=db, id=id)

    if not game:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="EL juego no existe"
        )

    repositorie_videogame_delete(db=db, id=id)

    return {"msg": "Juego eliminado"}