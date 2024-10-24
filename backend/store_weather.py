# backend/store_weather.py
import mysql.connector
from config import DB_CONFIG
from datetime import datetime

def store_weather_data(city, weather_data):
    """Store processed weather data into MySQL database."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO weather (city, temperature, weather_condition, timestamp)
    VALUES (%s, %s, %s, %s)
    """
    
    # Convert Unix timestamp to MySQL-compatible datetime format
    timestamp = datetime.utcfromtimestamp(weather_data['time']).strftime('%Y-%m-%d %H:%M:%S')
    
    # Insert data into MySQL
    cursor.execute(insert_query, (city, weather_data['temperature'], weather_data['weather'], timestamp))
    conn.commit()
    
    cursor.close()
    conn.close()
    print(f"Weather data for {city} has been stored successfully.")

# Example usage
if __name__ == "__main__":
    sample_processed_data = {
        'temperature': 27.0,
        'weather': 'Clear',
        'time': 1631782400
    }
    
    store_weather_data("Delhi", sample_processed_data)
