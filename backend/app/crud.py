from sqlalchemy.orm import Session
from .models import WeatherSearch


# CREATE
def create_weather_search(db: Session, data: dict):

    record = WeatherSearch(
        location=data.get("location"),
        country=data.get("country"),
        latitude=data.get("latitude"),
        longitude=data.get("longitude"),
        temperature=data.get("temperature"),
        windspeed=data.get("windspeed"),
        weathercode=data.get("weathercode")
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record


# READ ALL
def get_all_weather_searches(db: Session):
    return db.query(WeatherSearch).all()


# READ ONE
def get_weather_search_by_id(db: Session, record_id: int):
    return (
        db.query(WeatherSearch)
        .filter(WeatherSearch.id == record_id)
        .first()
    )


# UPDATE
def update_weather_search(db: Session, record_id: int, data: dict):

    record = (
        db.query(WeatherSearch)
        .filter(WeatherSearch.id == record_id)
        .first()
    )

    if not record:
        return None

    record.location = data.get("location", record.location)
    record.country = data.get("country", record.country)
    record.temperature = data.get("temperature", record.temperature)
    record.windspeed = data.get("windspeed", record.windspeed)

    db.commit()
    db.refresh(record)

    return record


# DELETE
def delete_weather_search(db: Session, record_id: int):

    record = (
        db.query(WeatherSearch)
        .filter(WeatherSearch.id == record_id)
        .first()
    )

    if not record:
        return None

    db.delete(record)
    db.commit()

    return {"message": "Deleted successfully"}