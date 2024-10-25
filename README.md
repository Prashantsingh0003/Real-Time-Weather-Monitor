
# Real-Time Weather Monitoring System with Rollups and Aggregates

This project is a real-time weather monitoring system using data from the [OpenWeatherMap API](https://openweathermap.org/), providing weather insights like daily summaries and alerts. The backend is built with Flask, and MySQL is used for data persistence.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [System Requirements](#system-requirements)
4. [Setup Instructions](#setup-instructions)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Testing](#testing)
8. [Contributing](#contributing)
9. [License](#license)

## Project Overview
The system fetches real-time weather data for major cities (Delhi, Mumbai, Chennai, Bangalore, Kolkata, Hyderabad, Berlin) at configurable intervals. The data is used to calculate daily rollups, detect threshold-based alerts, and provide visual insights.
![image](https://github.com/user-attachments/assets/b9d220ed-d3c9-4e92-9726-898a3820b8ca)

## Key Features
- **Real-Time Data Fetching**: Fetches data continuously from OpenWeatherMap API.
- **Daily Rollups and Aggregates**:
  - **Average Temperature**
  - **Dominant Weather Condition**
- **Threshold-Based Alerts**: User-defined temperature and weather condition thresholds.

## System Requirements
- **Programming Language**: Python 3.x
- **Framework**: Flask
- **Database**: MySQL (for data persistence)
- **Libraries**: See `requirements.txt`

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Prashantsingh0003/Real-Time-Weather-Monitoring.git
   cd Real-Time-Weather-Monitoring
Obtain an OpenWeatherMap API Key

Register at OpenWeatherMap to get an API key.
Update config.json or .env with your API key.
Install Dependencies

Using pip:
pip install -r requirements.txt
Set Up MySQL Database

Ensure MySQL is installed and running.
Create a database and user:
CREATE DATABASE weather_data;
CREATE USER 'weather_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON weather_data.* TO 'weather_user'@'localhost';
Update config.json or .env with database credentials.
Initialize the Database Schema

Run init_db.py to create necessary tables:
python init_db.py
Configuration
Configure the following parameters in config.json:

API Key: OpenWeatherMap API key.
Update Interval: Interval (in minutes) for data retrieval.
Thresholds: User-defined temperature/weather condition thresholds.
Database Config: MySQL settings (host, port, username, password, database).
Usage
Run the Flask application:

python app.py
![image](https://github.com/user-attachments/assets/e287d1dc-8010-47e2-93c8-7c124e15a132)

![image](https://github.com/user-attachments/assets/1844ee42-6d0c-453e-95f2-14603ff38bcb)


The application will start, retrieving weather data at specified intervals, storing rollups, and generating alerts when thresholds are met.
Access the web interface at http://localhost:5000.
Testing
This project includes test cases for:

System Initialization: Ensures Flask app and API connectivity.
Data Retrieval: Simulates API calls for weather data.
Alerts: Confirms alert generation when thresholds are breached.
Run tests using:

pytest tests/
Contributing
Contributions are welcome! Please create a pull request or open an issue for suggestions.
