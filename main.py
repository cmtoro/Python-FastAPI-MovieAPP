from fastapi import FastAPI
from middlewares.error_handler import ErrorHandler
from routers.movie_router import movie_router
from routers.auth_router import auth_router

app = FastAPI()
app.title = "My Movie API!"

#app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(auth_router)
