from pydantic import BaseModel


class WeatherCreate(BaseModel):
    location: str
    start_date: str
    end_date: str


class WeatherUpdate(BaseModel):
    location: str
    start_date: str
    end_date: str


class WeatherResponse(BaseModel):
    id: int
    location: str
    start_date: str
    end_date: str

    class Config:
        from_attributes = True