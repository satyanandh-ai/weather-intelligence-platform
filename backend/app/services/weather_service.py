import httpx

BASE_URL = "https://api.open-meteo.com/v1/forecast"


async def get_weather(lat: float, lon: float):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            BASE_URL,
            params={
                "latitude": lat,
                "longitude": lon,
                "current_weather": True
            }
        )
        return response.json()


async def get_forecast(lat: float, lon: float):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            BASE_URL,
            params={
                "latitude": lat,
                "longitude": lon,
                "daily": "temperature_2m_max,temperature_2m_min",
                "forecast_days": 5,
                "timezone": "auto"
            }
        )
        return response.json()