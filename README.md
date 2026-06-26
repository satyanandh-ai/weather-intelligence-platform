:::writing{variant="document" id="48291"}
🌦 Weather Intelligence Platform

A FastAPI-based backend system that provides real-time weather data, 5-day forecasts, full CRUD operations with database persistence, and export capabilities (JSON & CSV).
Built as part of an AI Engineer Internship Technical Assessment.

🚀 Features
🌍 Weather APIs
Get current weather by city
Get weather by GPS coordinates
5-day weather forecast
Google Maps integration for location visualization
🗄 CRUD Operations (Database)
Create weather search records
Read all / single records
Update existing records
Delete records
📤 Data Export
Export all stored records as JSON
Export all stored records as CSV
⚡ External API Integration
Uses Open-Meteo API for real-time weather data
Provides structured weather insights (temperature, windspeed, etc.)
🏗 Tech Stack
Backend: FastAPI
Database: SQLite (SQLAlchemy ORM)
HTTP Client: httpx
Language: Python 3.10+
API Docs: Swagger / OpenAPI
📂 Project Structure

backend/
└── app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── services/
│ └── weather\_service.py
└── routers/
└── weather.py

⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/satyanandh-ai/weather-intelligence-platform.git
cd weather-intelligence-platform
2. Create virtual environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate
3. Install dependencies
pip install fastapi uvicorn sqlalchemy httpx
4. Run the server
uvicorn backend.app.main:app --reload
5. Open API Docs
http://127.0.0.1:8000/docs
📡 API Endpoints
Weather APIs
GET /weather/current/{city}
GET /weather/forecast/{city}
GET /weather/current/coords
CRUD APIs
GET /weather/
POST /weather/
GET /weather/{record_id}
PUT /weather/{record_id}
DELETE /weather/{record_id}
Export APIs
GET /export/json
GET /export/csv
📊 Example Response
{
  "city": "Tokyo",
  "latitude": 35.6895,
  "longitude": 139.6917,
  "map": "https://www.google.com/maps?q=35.6895,139.6917",
  "weather": {
    "temperature": 21.5,
    "windspeed": 4.2
  }
}
🎯 Highlights (Why this project stands out)
Full backend system with real API integration
Clean RESTful architecture
Database persistence with CRUD operations
Export functionality for analytics use cases
Modular FastAPI design (services, routers, models)
👨‍💻 Author

Satya Anandh
AI/ML Engineer | FastAPI | Agentic AI Systems

GitHub: https://github.com/satyanandh-ai

📌 Notes
Built for internship assessment submission
Designed to demonstrate backend + API integration skills
Can be extended with frontend (React/Next.js) for full-stack version

:::

🟢 DONE