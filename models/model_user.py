from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import DateTime
from typing import List

from database.client import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100), 
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(100), 
        nullable=False,
        unique=True
    )

    password: Mapped[str] = mapped_column(
        String(100), 
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    videogames: Mapped[List["Videogame"]] = relationship(

        back_populates="user",

        cascade="all, delete-orphan"

    )