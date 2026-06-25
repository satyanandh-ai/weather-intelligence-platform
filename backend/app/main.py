from fastapi import FastAPI

from .database import Base, engine

app = FastAPI(
    title="Weather Intelligence Platform"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "message": "Weather Intelligence Platform API is running"
    }