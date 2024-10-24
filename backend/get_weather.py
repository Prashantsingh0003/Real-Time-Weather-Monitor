import requests
from config import API_KEY

def get_weather(city_name):
    """Fetch weather data from OpenWeatherMap for a given city."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': API_KEY  # Use the API key from config.py
    }
    
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: Failed to fetch weather data for {city_name}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":  # Corrected block
    city = "Delhi"
    weather_data = get_weather(city)
    print(weather_data)