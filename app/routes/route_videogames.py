from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Annotated

from app.services.services_videogames import services_add_game, services_games_get, services_get_game_by_title, services_get_game_by_id, services_delete_game, services_upgrade_game
from app.utils.security import validate_token
from app.schemas.schemas_videogames import GameForm, VideogameUpgrade
from app.schemas.schemas_user import UserResponse
from app.database.client import get_db

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
async def route_add_videogames(data: GameForm, user_current: Annotated[UserResponse, Depends(validate_token)], db: Session = Depends(get_db)):
    return services_add_game(
        title=data.title,
        description=data.description,
        version=data.version,
        owner_id=user_current.id,
        url_download=data.url_download, 
        db=db
    )


@route.patch('/')
async def route_upgrade_game(title: str, data: VideogameUpgrade, user_current: Annotated[UserResponse, Depends(validate_token)], db: Session = Depends(get_db)):
    return services_upgrade_game(
        title=title,
        new_title=data.title,
        description=data.description,
        version=data.version,
        url_download=data.url_download,
        db=db,
        user_current=user_current.id
    )


@route.delete("/{id}")
async def route_get_game_by_id(id:str, user_current: Annotated[UserResponse, Depends(validate_token)], db: Session = Depends(get_db)):
    return services_delete_game(
        id=id, 
        db=db, 
        user_current=user_current.id
    )


