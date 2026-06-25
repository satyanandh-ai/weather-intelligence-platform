from sqlalchemy import Column, Integer, String
from .database import Base


class WeatherSearch(Base):
    __tablename__ = "weather_searches"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=False)
    start_date = Column(String)
    end_date = Column(String)