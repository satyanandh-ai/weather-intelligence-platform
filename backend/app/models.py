from sqlalchemy import Column, Integer, String, Float
from .database import Base


class WeatherSearch(Base):
    __tablename__ = "weather_searches"

    id = Column(Integer, primary_key=True, index=True)

    location = Column(String, nullable=False)
    country = Column(String)

    start_date = Column(String)
    end_date = Column(String)

    latitude = Column(Float)
    longitude = Column(Float)

    temperature = Column(Float)
    windspeed = Column(Float)
    weathercode = Column(Integer)