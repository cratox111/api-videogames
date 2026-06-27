from fastapi import FastAPI
from database.client import Base, engine
from routes import route_user, route_videogames

app = FastAPI()

app.include_router(router=route_user.route)
app.include_router(router=route_videogames.route)

Base.metadata.create_all(bind=engine)

@app.get('/')
async def root():
    return {"msg": "Hola fastapi"}