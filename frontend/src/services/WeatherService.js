// src/services/WeatherService.js
const API_URL = "/weather";  // Proxy should handle localhost:5000

export async function fetchWeatherData(city) {
    try {
        const response = await fetch(`${API_URL}/${city}`);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error fetching weather data:", error);
        return null;
    }
}
