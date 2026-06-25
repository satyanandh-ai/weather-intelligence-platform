from fastapi import FastAPI

from .database import Base, engine
from .routers.weather import router as weather_router

app = FastAPI(
    title="Weather Intelligence Platform"
)

Base.metadata.create_all(bind=engine)

app.include_router(weather_router)

@app.get("/")
def root():
    return {
        "message": "Weather Intelligence Platform API is running"
    }