from pydantic import BaseModel, Field, ConfigDict


class GameStudioCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    country: str = Field(min_length=2, max_length=100)


class GameStudioResponse(GameStudioCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class GameCreate(BaseModel):
    title: str = Field(min_length=2, max_length=100)

    desc: str = Field(
        min_length=2,
        max_length=500
    )

    rec_age: int = Field(
        ge=0,
        le=18
    )

    genre: str = Field(
        min_length=2,
        max_length=50
    )

    price: int = Field(
        ge=0
    )

    studio_id: int = Field(
        gt=0
    )


class GameResponse(GameCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)