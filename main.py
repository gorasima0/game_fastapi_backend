from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas

from database import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# =====================================
# GAME STUDIO
# =====================================


@app.post(
    "/create_studio",
    response_model=schemas.GameStudioResponse
)
def create_studio(
    studio: schemas.GameStudioCreate,
    db: Session = Depends(get_db)
):
    new_studio = models.GameStudio(
        name=studio.name,
        country=studio.country
    )

    db.add(new_studio)
    db.commit()
    db.refresh(new_studio)

    return new_studio


@app.get("/studios")
def get_studios(
    db: Session = Depends(get_db)
):
    studios = db.query(models.GameStudio).all()

    return studios


@app.get("/studios/{studio_id}")
def get_studio_by_id(
    studio_id: int,
    db: Session = Depends(get_db)
):
    studio = db.query(models.GameStudio).filter(
        models.GameStudio.id == studio_id
    ).first()

    if studio is None:
        raise HTTPException(
            status_code=404,
            detail="Studio not found!"
        )

    return studio


@app.delete("/studios/{studio_id}")
def delete_studio(
    studio_id: int,
    db: Session = Depends(get_db)
):
    studio = db.query(models.GameStudio).filter(
        models.GameStudio.id == studio_id
    ).first()

    if studio is None:
        raise HTTPException(
            status_code=404,
            detail="Studio not found!"
        )

    db.delete(studio)
    db.commit()

    return {
        "message": "Studio deleted!"
    }


# =====================================
# GAME
# =====================================


@app.post(
    "/create_game",
    response_model=schemas.GameResponse
)
def create_game(
    game: schemas.GameCreate,
    db: Session = Depends(get_db)
):
    studio = db.query(models.GameStudio).filter(
        models.GameStudio.id == game.studio_id
    ).first()

    if studio is None:
        raise HTTPException(
            status_code=404,
            detail="Studio not found!"
        )

    new_game = models.Game(
        title=game.title,
        desc=game.desc,
        rec_age=game.rec_age,
        genre=game.genre,
        price=game.price,
        studio_id=game.studio_id
    )

    db.add(new_game)
    db.commit()
    db.refresh(new_game)

    return new_game


@app.get("/games")
def get_games(
    db: Session = Depends(get_db)
):
    games = db.query(models.Game).all()

    return games


@app.get("/games/{game_id}")
def get_game_by_id(
    game_id: int,
    db: Session = Depends(get_db)
):
    game = db.query(models.Game).filter(
        models.Game.id == game_id
    ).first()

    if game is None:
        raise HTTPException(
            status_code=404,
            detail="Game not found!"
        )

    return game


@app.delete("/games/{game_id}")
def delete_game(
    game_id: int,
    db: Session = Depends(get_db)
):
    game = db.query(models.Game).filter(
        models.Game.id == game_id
    ).first()

    if game is None:
        raise HTTPException(
            status_code=404,
            detail="Game not found!"
        )

    db.delete(game)
    db.commit()

    return {
        "message": "Game deleted!"
    }