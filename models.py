from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class GameStudio(Base):
    __tablename__ = "game_studios"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)

    games = relationship(
        "Game",
        back_populates="studio",
        cascade="all, delete-orphan"
    )


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    desc = Column(String, nullable=False)
    rec_age = Column(Integer, nullable=False)
    genre = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    studio_id = Column(
        Integer,
        ForeignKey("game_studios.id"),
        nullable=False
    )

    studio = relationship(
        "GameStudio",
        back_populates="games"
    )