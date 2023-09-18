from typing import Optional
from pydantic import BaseModel, Field

class Movie(BaseModel):
    movie_id: Optional[int] = None
    title: str = Field(max_length=50, min_length=5)
    overview: str = Field(max_length=200, min_length=15)
    year: int = Field(le=2023, ge=1900)
    rating: float = Field(le=10, ge=1)
    category: str = Field(min_length=3, max_length=50)

    model_config = {
        "json_schema_extra": {
            "example": {
                "movie_id": 1,
                "title": "Mi Película",
                "overview": "Descripción de la película",
                "year": 2022,
                "rating": 9.9,
                "category": "Acción"
            }
        }
    }