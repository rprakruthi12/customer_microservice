from pydantic import BaseModel, Field
from typing import Optional

class StoreBase(BaseModel):
    store_name: str = Field(..., min_length=1, max_length=100)
    location: str = Field(..., min_length=1, max_length=255)

class StoreCreate(StoreBase):
    pass

class Store(StoreBase):
    store_id: int

    class Config:
        orm_mode = True

class AvailabilityBase(BaseModel):
    store_id: int = Field(..., gt=0)
    film_id: int = Field(..., gt=0)

class AvailabilityCreate(AvailabilityBase):
    pass

class Availability(AvailabilityBase):
    availability_id: int

    class Config:
        orm_mode = True

class FilmBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    release_year: int = Field(..., ge=1900, le=2024)
    genre: str = Field(..., min_length=1, max_length=50)

class FilmCreate(FilmBase):
    pass

class Film(FilmBase):
    film_id: int

    class Config:
        orm_mode = True

class FilmActorBase(BaseModel):
    film_id: int = Field(..., gt=0)
    actor_name: str = Field(..., min_length=1, max_length=100)

class FilmActorCreate(FilmActorBase):
    pass

class FilmActor(FilmActorBase):
    actor_id: int

    class Config:
        orm_mode = True

class StoreWithFilm(BaseModel):
    store_id: int
    store_name: str
    location: str
    film_name: Optional[str] = None

    class Config:
        orm_mode = True
