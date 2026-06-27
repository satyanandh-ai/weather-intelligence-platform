from sqlalchemy.orm import Session
from datetime import datetime
from .models import WeatherSearch


# -----------------------------
# CREATE
# -----------------------------
def create_weather_search(
    db: Session,
    location: str,
    country: str,
    start_date: str,
    end_date: str,
    latitude: float,
    longitude: float,
    temperature: float,
    windspeed: float,
    weathercode: int
):

    # Validate date format
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        return {
            "error": "Invalid date format. Use YYYY-MM-DD"
        }

    # Validate date range
    if start > end:
        return {
            "error": "start_date cannot be greater than end_date"
        }

    record = WeatherSearch(
        location=location,
        country=country,
        start_date=start_date,
        end_date=end_date,
        latitude=latitude,
        longitude=longitude,
        temperature=temperature,
        windspeed=windspeed,
        weathercode=weathercode
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


# -----------------------------
# READ ALL
# -----------------------------
def get_all_weather_searches(db: Session):
    return db.query(WeatherSearch).all()


# -----------------------------
# READ BY ID
# -----------------------------
def get_weather_search_by_id(
    db: Session,
    record_id: int
):
    return (
        db.query(WeatherSearch)
        .filter(WeatherSearch.id == record_id)
        .first()
    )


# -----------------------------
# UPDATE
# -----------------------------
def update_weather_search(
    db: Session,
    record_id: int,
    location: str,
    country: str,
    temperature: float,
    windspeed: float
):

    record = (
        db.query(WeatherSearch)
        .filter(WeatherSearch.id == record_id)
        .first()
    )

    if not record:
        return {
            "error": "Record not found"
        }

    record.location = location
    record.country = country
    record.temperature = temperature
    record.windspeed = windspeed

    db.commit()
    db.refresh(record)

    return record


# -----------------------------
# DELETE
# -----------------------------
def delete_weather_search(
    db: Session,
    record_id: int
):

    record = (
        db.query(WeatherSearch)
        .filter(WeatherSearch.id == record_id)
        .first()
    )

    if not record:
        return {
            "error": "Record not found"
        }

    db.delete(record)
    db.commit()

    return {
        "message": "Record deleted successfully"
    }