// src/components/WeatherCard.js
import React from 'react';
import './WeatherCard.css'; // Import CSS for the weather card

const WeatherCard = ({ weatherData, city }) => {
    return (
        <div className="WeatherCard">
            <h2>Weather in {city}</h2>
            <p>Temperature: {weatherData.temperature.toFixed(2)}°C</p>
            <p>Condition: {weatherData.weather}</p>
            <p>Last Updated: {new Date(weatherData.time * 1000).toLocaleString()}</p>
        </div>
    );
};

export default WeatherCard;
