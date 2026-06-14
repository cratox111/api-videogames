from fastapi import FastAPI
from database.client import Base, engine
from models.model_user import User
from routes import route_user

app = FastAPI()

app.include_router(router=route_user.route)

Base.metadata.create_all(bind=engine)

@app.get('/')
async def root():
    return {"msg": "Hola fastapi"}