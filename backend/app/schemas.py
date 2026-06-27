from pydantic import BaseModel


class WeatherCreate(BaseModel):
    location: str
    country: str
    start_date: str
    end_date: str
    latitude: float
    longitude: float
    temperature: float
    windspeed: float
    weathercode: int


class WeatherUpdate(BaseModel):
    location: str
    country: str
    temperature: float
    windspeed: float


class WeatherResponse(BaseModel):
    id: int

    location: str
    country: str

    start_date: str
    end_date: str

    latitude: float
    longitude: float

    temperature: float
    windspeed: float
    weathercode: int

    class Config:
        from_attributes = True