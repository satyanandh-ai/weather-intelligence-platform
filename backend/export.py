from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import csv
import io

from ..database import get_db
from ..models import WeatherSearch

router = APIRouter(prefix="/export", tags=["Export"])


@router.get("/json")
def export_json(db: Session = Depends(get_db)):
    records = db.query(WeatherSearch).all()

    return {
        "data": [
            {
                "id": r.id,
                "location": r.location,
                "country": r.country,
                "temperature": r.temperature,
                "windspeed": r.windspeed
            }
            for r in records
        ]
    }


@router.get("/csv")
def export_csv(db: Session = Depends(get_db)):
    records = db.query(WeatherSearch).all()

    output = io.StringIO()
    writer = csv.writer(output)

    writer.writerow(["id", "location", "country", "temperature", "windspeed"])

    for r in records:
        writer.writerow([
            r.id,
            r.location,
            r.country,
            r.temperature,
            r.windspeed
        ])

    return {"file": output.getvalue()}