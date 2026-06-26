from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import WeatherCreate, WeatherUpdate
from ..crud import (
    create_weather_search,
    get_all_weather_searches,
    get_weather_search_by_id,
    update_weather_search,
    delete_weather_search
)
from ..services.weather_service import get_weather, get_forecast

router = APIRouter(prefix="/weather", tags=["Weather"])

CITY_COORDS = {
    "Tokyo": (35.6895, 139.6917),
    "London": (51.5074, -0.1278),
    "New York": (40.7128, -74.0060),
    "Delhi": (28.7041, 77.1025),
    "Cuddapah": (14.47, 78.82),
}


# --------------------
# CRUD ENDPOINTS
# --------------------

@router.post("/")
def create_weather(
    weather: WeatherCreate,
    db: Session = Depends(get_db)
):
    return create_weather_search(
        db,
        weather.model_dump()
    )


@router.get("/")
def get_all(
    db: Session = Depends(get_db)
):
    return get_all_weather_searches(db)


@router.get("/{record_id}")
def get_by_id(
    record_id: int,
    db: Session = Depends(get_db)
):
    return get_weather_search_by_id(
        db,
        record_id
    )


@router.put("/{record_id}")
def update(
    record_id: int,
    weather: WeatherUpdate,
    db: Session = Depends(get_db)
):
    return update_weather_search(
        db,
        record_id,
        weather.model_dump(exclude_unset=True)
    )


@router.delete("/{record_id}")
def delete(
    record_id: int,
    db: Session = Depends(get_db)
):
    return delete_weather_search(
        db,
        record_id
    )


# --------------------
# CURRENT WEATHER
# --------------------

@router.get("/current/{city}")
async def current_weather(city: str):

    city = city.title()

    if city not in CITY_COORDS:
        return {
            "error": "City not supported",
            "available": list(CITY_COORDS.keys())
        }

    lat, lon = CITY_COORDS[city]

    weather = await get_weather(lat, lon)

    map_url = f"https://www.google.com/maps?q={lat},{lon}"

    return {
        "city": city,
        "latitude": lat,
        "longitude": lon,
        "map": map_url,
        "weather": weather
    }


# --------------------
# FORECAST
# --------------------

@router.get("/forecast/{city}")
async def forecast(city: str):

    city = city.title()

    if city not in CITY_COORDS:
        return {
            "error": "City not supported",
            "available": list(CITY_COORDS.keys())
        }

    lat, lon = CITY_COORDS[city]

    forecast_data = await get_forecast(lat, lon)

    map_url = f"https://www.google.com/maps?q={lat},{lon}"

    return {
        "city": city,
        "latitude": lat,
        "longitude": lon,
        "map": map_url,
        "forecast": forecast_data
    }