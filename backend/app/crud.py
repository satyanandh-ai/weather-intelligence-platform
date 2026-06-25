from sqlalchemy.orm import Session
from .models import WeatherSearch


# CREATE
def create_weather_search(
    db: Session,
    location: str,
    start_date: str,
    end_date: str
):
    weather_record = WeatherSearch(
        location=location,
        start_date=start_date,
        end_date=end_date
    )

    db.add(weather_record)
    db.commit()
    db.refresh(weather_record)

    return weather_record


# READ ALL
def get_all_weather_searches(db: Session):
    return db.query(WeatherSearch).all()


# READ BY ID
def get_weather_search_by_id(
    db: Session,
    record_id: int
):
    return (
        db.query(WeatherSearch)
        .filter(WeatherSearch.id == record_id)
        .first()
    )


# UPDATE
def update_weather_search(
    db: Session,
    record_id: int,
    location: str,
    start_date: str,
    end_date: str
):
    record = (
        db.query(WeatherSearch)
        .filter(WeatherSearch.id == record_id)
        .first()
    )

    if not record:
        return {"error": "Record not found"}

    record.location = location
    record.start_date = start_date
    record.end_date = end_date

    db.commit()
    db.refresh(record)

    return record


# DELETE
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
        return {"error": "Record not found"}

    db.delete(record)
    db.commit()

    return {
        "message": "Record deleted successfully"
    }