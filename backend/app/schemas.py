from pydantic import BaseModel


class WeatherCreate(BaseModel):
    location: str
    country: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    temperature: float | None = None
    windspeed: float | None = None
    weathercode: int | None = None


class WeatherUpdate(BaseModel):
    location: str | None = None
    country: str | None = None
    temperature: float | None = None
    windspeed: float | None = None


class WeatherResponse(BaseModel):
    id: int
    location: str
    country: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    temperature: float | None = None
    windspeed: float | None = None
    weathercode: int | None = None

    class Config:
        from_attributes = True