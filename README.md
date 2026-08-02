# Plataforma de Videojuegos API

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
- routes/
Se encarga de obtener la informacion enviada por el cliente y obtiene las dependecias necesarias y de vuelve la respuesta al cliente. Pero en el no hay nada de logica o DB.

- services/
Este se encarga de realizar toda la logica de la API. Desde la logica de negocio de user y Videogames y el sistema de logeo.

- repositories/
Se encargan del acceso a la base de datos utilizando SQLAlchemy.
Aquí se realizan consultas, inserciones, actualizaciones y eliminaciones de registros..

- models/
Definen las tablas de la base de datos mediante el ORM de SQLAlchemy y las relaciones entre ellas.

- schemas/
Definen los modelos de Pydantic utilizados para validar los datos de entrada y estructurar las respuestas enviadas al cliente.

- database/
Este se encarga de la conexiones de la DB aqui se Crea el motor del cual derivan las Session

- utils/
Contiene utilidades reutilizables que pueden ser utilizadas desde distintos módulos del proyecto, por ejemplo funciones relacionadas con seguridad o definición de tipos.

# Instalacion
git clone https://github.com/cratox111/api-videogames.git

cd backend_plataforma

python -m venv .venv

pip install -r requirements.txt

uvicorn main:app --reload