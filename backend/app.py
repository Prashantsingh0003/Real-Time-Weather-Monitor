# backend/app.py
from flask import Flask, jsonify
from get_weather import get_weather
from process_weather import process_weather_data
from store_weather import store_weather_data

app = Flask(__name__)

@app.route('/weather/<city>', methods=['GET'])
def fetch_weather(city):
    """Fetch, process, and store weather data for a city."""
    raw_data = get_weather(city)
    if raw_data:
        processed_data = process_weather_data(raw_data)
        store_weather_data(city, processed_data)
        return jsonify(processed_data)
    else:
        return jsonify({"error": "Failed to fetch weather data"}), 500

if __name__ == "__main__":
    app.run(debug=True)
