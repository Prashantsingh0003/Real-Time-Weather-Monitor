# backend/process_weather.py

def process_weather_data(data):
    """Process the raw weather data and extract relevant details."""
    if data:
        temp_kelvin = data['main']['temp']
        temp_celsius = temp_kelvin - 273.15  # Kelvin to Celsius conversion
        weather_condition = data['weather'][0]['main']
        timestamp = data['dt']  # Unix timestamp
        
        # Return processed data as a dictionary
        return {
            'temperature': temp_celsius,
            'weather': weather_condition,
            'time': timestamp
        }
    return None

# Example usage
if __name__ == "__main__":
    sample_data = {
        "main": {
            "temp": 300.15
        },
        "weather": [
            {"main": "Clear"}
        ],
        "dt": 1631782400
    }
    
    processed_data = process_weather_data(sample_data)
    print(processed_data)
