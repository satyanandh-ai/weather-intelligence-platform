from fastapi import FastAPI
from .database import Base, engine

from .routers.weather import router as weather_router
from .routers.export import router as export_router

app = FastAPI(title="Weather Intelligence Platform")

Base.metadata.create_all(bind=engine)

app.include_router(weather_router)
app.include_router(export_router)


@app.get("/")
def root():
    return {"message": "API running"}