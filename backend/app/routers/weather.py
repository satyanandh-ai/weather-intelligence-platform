from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import requests

from .. import crud
from ..schemas import WeatherCreate, WeatherUpdate
from ..dependencies import get_db

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)


# CREATE
@router.post("/")
def create_weather(
    weather: WeatherCreate,
    db: Session = Depends(get_db)
):
    return crud.create_weather_search(
        db,
        weather.location,
        weather.start_date,
        weather.end_date
    )


# READ ALL
@router.get("/")
def get_all_weather(
    db: Session = Depends(get_db)
):
    return crud.get_all_weather_searches(db)


# READ BY ID
@router.get("/{record_id}")
def get_weather_by_id(
    record_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_weather_search_by_id(
        db,
        record_id
    )


# UPDATE
@router.put("/{record_id}")
def update_weather(
    record_id: int,
    weather: WeatherUpdate,
    db: Session = Depends(get_db)
):
    return crud.update_weather_search(
        db,
        record_id,
        weather.location,
        weather.start_date,
        weather.end_date
    )


# DELETE
@router.delete("/{record_id}")
def delete_weather(
    record_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_weather_search(
        db,
        record_id
    )


# CURRENT WEATHER API
@router.get("/current/{city}")
def get_current_weather(city: str):

    geocode_url = (
        f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    )

    geo_response = requests.get(geocode_url).json()

    if "results" not in geo_response:
        return {
            "error": "Location not found"
        }

    location_data = geo_response["results"][0]

    latitude = location_data["latitude"]
    longitude = location_data["longitude"]

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current_weather=true"
    )

    weather_response = requests.get(weather_url).json()

    return {
        "city": city,
        "country": location_data.get("country"),
        "latitude": latitude,
        "longitude": longitude,
        "weather": weather_response
    }