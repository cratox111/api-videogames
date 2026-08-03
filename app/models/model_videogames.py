from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import DateTime
from typing import Optional

from app.database.client import Base


# Crea el modelo Videogames para hacer referencia a la Tabla SQL
class Videogame(Base):
    __tablename__ = "videogames"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    title: Mapped[str] = mapped_column(
        String(100), 
        nullable=False
    )


    description: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    version: Mapped[str] = mapped_column(
        String(10),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    likes_count: Mapped[Optional[int]] = mapped_column(
        Integer,
        default=0
    )

    url_download: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    # Le dice que esta columna referencia a la columna id en la tabla user
    owner_id: Mapped[int] = mapped_column(

        ForeignKey("users.id")

    )

    # Crea la relacion con la tabla 'user'
    user: Mapped["User"] = relationship(

        back_populates="videogames"

    )
