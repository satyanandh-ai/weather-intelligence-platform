from fastapi import FastAPI

from .database import Base, engine
from .routers import weather
from .routers import export

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Weather Intelligence Platform",
    version="0.1.0"
)

app.include_router(weather.router)
app.include_router(export.router)


@app.get("/")
def root():
    return {"message": "API running"}