from sqlalchemy import Column, Integer, String, Float
from .database import Base


class WeatherSearch(Base):
    __tablename__ = "weather_searches"

    id = Column(Integer, primary_key=True, index=True)

    location = Column(String, nullable=False)
    country = Column(String, nullable=True)

    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    temperature = Column(Float, nullable=True)
    windspeed = Column(Float, nullable=True)
    weathercode = Column(Integer, nullable=True)