from fastapi import APIRouter, Path, Query, Depends
from config.database import movies_collection
from typing import List
from fastapi.responses import JSONResponse
from middlewares.jwt_bearer import JWTBearer
from models.movie_model import Movie
from services.movie_service import MovieService

movie_router = APIRouter()

@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    movie_list = list(MovieService(movies_collection).get_movies())
    return JSONResponse(status_code=200, content=movie_list)

@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=200)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    movie_by_id = MovieService(movies_collection).get_movie_by_id(id)
    return JSONResponse(status_code=200, content=[]) if movie_by_id == None else JSONResponse(status_code=200, content=dict(movie_by_id))

@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies_by_parameters(category: str = Query(min_length=3, max_length=20), year: int = Query(le=2023, ge=1900)) -> List[Movie]:
    movie_list = MovieService(movies_collection).get_movie_by_params(category, year)
    return JSONResponse(status_code=200, content=list(movie_list))

@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    result = MovieService(movies_collection).create_movie(movie)
    return JSONResponse(status_code=201, content={'message': 'Se ha creado la película. ' + str(result.inserted_id)})

@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie) -> dict:
    result = MovieService(movies_collection).update_movie(id, movie)
    if result.acknowledged and result.modified_count == 1:
        return JSONResponse(status_code=200, content={'message': 'Se ha actualizado la película ' + movie.title})
    return JSONResponse(status_code=404, content={'message': 'No se ha encontrado la película con id ' + str(id)})

@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movie(id: int) -> dict:
    result = MovieService(movies_collection).delete_movie(id)
    if result.acknowledged and result.deleted_count == 1:
        return JSONResponse(status_code=200, content={'message': 'Se ha eliminado la película con id ' + str(id)})
    return JSONResponse(status_code=404, content={'message': 'No se ha encontrado la película con id ' + str(id)})
    