# 🌦 Weather Intelligence Platform

A FastAPI-based backend system that delivers real-time weather data, 5-day forecasts, and full CRUD operations with database persistence and export capabilities.

Built as part of an AI Engineer Internship Technical Assessment.

---

## 🚀 Features

### 🌍 Weather APIs
- Get real-time weather by city name
- Get weather using GPS coordinates
- 5-day weather forecast
- Google Maps integration for each location

---

### 🗄 Database (CRUD System)
- Create weather search records
- Read all or specific records
- Update existing records
- Delete records

---

### 📤 Data Export
- Export stored data as JSON
- Export stored data as CSV

---

### 🌐 External API Integration
- Uses Open-Meteo API
- Provides real-time:
  - Temperature 🌡
  - Windspeed 💨
  - Weather conditions ☁️

---

## 🏗 Tech Stack

- FastAPI (Backend Framework)
- SQLite (Database)
- SQLAlchemy (ORM)
- httpx (API Requests)
- Python 3.10+

---

## 📂 Project Structure

backend/
└── app/
    ├── main.py
    ├── database.py
    ├── models.py
    ├── schemas.py
    ├── crud.py
    ├── services/
    │   └── weather_service.py
    └── routers/
        └── weather.py

---

## ⚙️ Setup Instructions

### 1. Clone Repository
git clone https://github.com/satyanandh-ai/weather-intelligence-platform.git
cd weather-intelligence-platform

---

### 2. Create Virtual Environment
python -m venv venv

Activate:
venv\Scripts\activate

---

### 3. Install Dependencies
pip install fastapi uvicorn sqlalchemy httpx

---

### 4. Run Server
uvicorn backend.app.main:app --reload

---

### 5. Open API Docs
http://127.0.0.1:8000/docs

---

## 📡 API Endpoints

### Weather APIs
GET /weather/current/{city}
GET /weather/forecast/{city}
GET /weather/current/coords

---

### CRUD APIs
GET /weather/
POST /weather/
GET /weather/{record_id}
PUT /weather/{record_id}
DELETE /weather/{record_id}

---

### Export APIs
GET /export/json
GET /export/csv

---

## 📊 Example Response

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

---

## 🧠 Highlights

- Clean REST API design
- Real-time weather integration
- Full CRUD with database
- Export system (JSON + CSV)
- Modular FastAPI architecture

---

## 👨‍💻 Author

Satya Anandh  
AI/ML Engineer | FastAPI | Agentic AI Systems

GitHub: https://github.com/satyanandh-ai

---

## 📌 Notes

- Built for internship submission
- Backend-focused project
- Can be extended to full-stack (React frontend possible)