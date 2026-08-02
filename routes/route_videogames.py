from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Annotated

from services.services_videogames import services_add_game, services_games_get, services_get_game_by_title, services_get_game_by_id, services_delete_game, services_upgrade_game
from services.services_auth import get_current_user, oauth
from schemas.schemas_videogames import GameForm, VideogameUpgrade
from database.client import get_db

route = APIRouter(prefix="/videogames", tags=["Videogames"])



@route.get("/id/{id}")
async def route_get_game_by_id(id:str, db: Session = Depends(get_db)):
    return services_get_game_by_id(id=id, db=db)


@route.get("/title/{title}")
async def route_get_game_by_title(title: str, db: Session = Depends(get_db)):
    return services_get_game_by_title(title=title, db=db)
                                      
                        
@route.get("/")
async def route_get_games(db: Session = Depends(get_db)):
    return services_games_get(db=db)

@route.post('/')
async def route_add_videogames(data: GameForm, token: Annotated[str, Depends(oauth)] ,db: Session = Depends(get_db)):
    return services_add_game(
        title=data.title,
        description=data.description,
        version=data.version,
        owner_id=get_current_user(token=token, db=db),
        url_download=data.url_download, 
        db=db
    )


@route.patch('/')
async def route_upgrade_game(title: str, data: VideogameUpgrade, token: Annotated[str, Depends(oauth)], db: Session = Depends(get_db)):
    return services_upgrade_game(
        title=title,
        new_title=data.title,
        description=data.description,
        version=data.version,
        url_download=data.url_download,
        db=db
    )


@route.delete("/{id}")
async def route_get_game_by_id(id:str, token: Annotated[str, Depends(oauth)], db: Session = Depends(get_db)):
    return services_delete_game(id=id, db=db)


