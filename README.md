# 🌦 Weather Intelligence Platform

## AI Engineer Internship Technical Assessment

A production-style weather intelligence backend built with **FastAPI**, **SQLite**, and **Open-Meteo API**.

The platform allows users to retrieve real-time weather data, view forecasts, store weather searches, manage historical records through CRUD operations, validate user input, and export weather data for further analysis.

---

# 🚀 Features

## 🌍 Real-Time Weather Data

* Current weather by city
* Current weather by GPS coordinates
* 5-day weather forecast
* Google Maps integration for location visualization

---

## 🗄 Database Persistence

Store weather search information including:

* Location
* Country
* Date range
* Coordinates
* Temperature
* Wind speed
* Weather code

SQLite is used for persistent storage via SQLAlchemy ORM.

---

## 🔄 CRUD Operations

### Create

Create and store weather search records.

### Read

View all previously stored weather searches or retrieve individual records.

### Update

Update weather information stored in the database.

### Delete

Remove records from the database.

---

## ✅ Validation

Implemented validation for:

* Invalid date formats
* Invalid date ranges
* Start date greater than end date

Example:

```json
{
  "error": "start_date cannot be greater than end_date"
}
```

---

## 📤 Export Features

Export stored weather data into:

### JSON

```http
GET /export/json
```

### CSV

```http
GET /export/csv
```

---

## 🌐 API Integration

### Open-Meteo API

Used for:

* Current weather
* Forecast retrieval

### Google Maps

Used for:

* Location visualization
* Coordinate mapping

---

# 🏗 Architecture

```text
Client
   │
   ▼
FastAPI Routes
   │
   ▼
Weather Service
   │
   ▼
Open-Meteo API
   │
   ▼
SQLite Database
```

---

# 📂 Project Structure

```text
weather-intelligence-platform/

├── backend/
│   └── app/
│       ├── main.py
│       ├── database.py
│       ├── models.py
│       ├── schemas.py
│       ├── crud.py
│       │
│       ├── services/
│       │   └── weather_service.py
│       │
│       └── routers/
│           ├── weather.py
│           └── export.py
│
├── requirements.txt
├── README.md
└── weather.db
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/satyanandh-ai/weather-intelligence-platform.git
cd weather-intelligence-platform
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
uvicorn backend.app.main:app --reload
```

---

# 📚 API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

OpenAPI Schema:

```text
http://127.0.0.1:8000/openapi.json
```

---

# 📡 Available Endpoints

## Weather APIs

| Method | Endpoint                 |
| ------ | ------------------------ |
| GET    | /weather/current/{city}  |
| GET    | /weather/forecast/{city} |
| GET    | /weather/current/coords  |

---

## CRUD APIs

| Method | Endpoint             |
| ------ | -------------------- |
| POST   | /weather/            |
| GET    | /weather/            |
| GET    | /weather/{record_id} |
| PUT    | /weather/{record_id} |
| DELETE | /weather/{record_id} |

---

## Export APIs

| Method | Endpoint     |
| ------ | ------------ |
| GET    | /export/json |
| GET    | /export/csv  |

---

# 🧪 Example Stored Record

```json
{
  "id": 2,
  "location": "Tokyo",
  "country": "Japan",
  "start_date": "2026-06-01",
  "end_date": "2026-06-05",
  "latitude": 35.6895,
  "longitude": 139.6917,
  "temperature": 21.5,
  "windspeed": 4.2,
  "weathercode": 55
}
```

---

# 🎯 Assessment Requirements Coverage

| Requirement             | Status |
| ----------------------- | ------ |
| REST API Development    | ✅      |
| CRUD Operations         | ✅      |
| SQL Database            | ✅      |
| Data Persistence        | ✅      |
| Weather API Integration | ✅      |
| Forecast Support        | ✅      |
| Date Validation         | ✅      |
| Google Maps Integration | ✅      |
| Export Functionality    | ✅      |
| Error Handling          | ✅      |
| OpenAPI Documentation   | ✅      |

---

# 🌟 PM Accelerator Mission

PM Accelerator helps aspiring professionals build real-world technical, product, and leadership skills through hands-on projects, mentorship, and industry-focused learning experiences.

This project was developed as part of the PM Accelerator AI Engineer Internship Technical Assessment.

---

# 👨‍💻 Author

**Satya Anandh**

AI/ML Engineer • FastAPI Developer • Agentic AI Builder

GitHub:
https://github.com/satyanandh-ai

LinkedIn:
(Add your LinkedIn profile link)

---

# 📄 License

This project is open source and available for educational and assessment purposes.
