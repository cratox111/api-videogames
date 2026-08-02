# Plataforma de Videojuegos API

## Contenido

- Descripción

- Tecnologías

- Arquitectura

- Instalación

- Variables de entorno

- Endpoints

- Autenticación

- Próximas mejoras

## Descripcion

API REST desarrollada con FastAPI para gestionar usuarios y videojuegos.
Incluye autenticación mediante JWT, PostgreSQL y SQLAlchemy siguiendo una arquitectura por capas.

## Tecnologias:
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- JWT
- Passlib
- Alembic (cuando lo agregues)

## Arquitectura:
- routes/:
Se encarga de obtener la informacion enviada por el cliente y obtiene las dependecias necesarias y de vuelve la respuesta al cliente. Pero en el no hay nada de logica o DB.

- services/:
Este se encarga de realizar toda la logica de la API. Desde la logica de negocio de user y Videogames y el sistema de logeo.

- repositories/:
Se encargan del acceso a la base de datos utilizando SQLAlchemy.
Aquí se realizan consultas, inserciones, actualizaciones y eliminaciones de registros..

- models/:
Definen las tablas de la base de datos mediante el ORM de SQLAlchemy y las relaciones entre ellas.

- schemas/:
Definen los modelos de Pydantic utilizados para validar los datos de entrada y estructurar las respuestas enviadas al cliente.

- database/:
Este se encarga de la conexiones de la DB aqui se Crea el motor del cual derivan las Session

- utils/:
Contiene utilidades reutilizables que pueden ser utilizadas desde distintos módulos del proyecto, por ejemplo funciones relacionadas con seguridad o definición de tipos.

## Instalacion
git clone https://github.com/cratox111/api-videogames.git

cd backend_plataforma

python -m venv .venv

pip install -r requirements.txt

uvicorn main:app --reload

## Variables de entorno
- DATABASE_URI: Contiene la URI de la DB.
- SECRET: Contiene una clave.
- ISS: Contiene quien emite los tokens.
- ACCESS_TOKEN_EXPIRE_MINUTES: Contiene la duracion de los tokens

## Endpoints importantes
GET /user/response: Obtiene la informacion del usuario actual. (Es necesario logearte)
GET /users: Obtiene todos los usuarios de la DB.
DELETE /user/{id}: Elimina a un juego usuario mediante el id. (Es necesario logearte)
POST /videogames: Añade un juego con la informacion que se le introdusca. (Es necesario logearte)
DELETE /videogames{id}: Elimina a un videojuego mediante el id. (Es necesario logearte)

## Autentificacion

1. Se obtiene el token de POST /auth/login
2. Se valida el token mediante la funcion validate_token(token, db)
3. De ser validado correctamente regresa un Objeto ResponseUser con la info del propietario del token
4. Esto es usa en los distintos endpoint que necesite saber el user_current

## Próximas mejoras

- Alembic
- Docker
- Tests

Cliente
   │
   ▼
Routes
   │
   ▼
Services
   │
   ▼
Repositories
   │
   ▼
SQLAlchemy
   │
   ▼
PostgreSQL

-------------------------------
Diego Ochoa Gonzalez