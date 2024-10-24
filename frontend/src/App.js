// src/App.js
import './App.css';
import React, { useState } from 'react';
import WeatherCard from './components/WeatherCard';
import { fetchWeatherData } from './services/WeatherService';

function App() {
    const [city, setCity] = useState('');
    const [weatherData, setWeatherData] = useState(null);

    const handleFetchWeather = async () => {
        const data = await fetchWeatherData(city);
        setWeatherData(data);
    };

    return (
        <div className="App">
            <h1>Real-Time Weather Monitor</h1>
            <div>
                <input
                    type="text"
                    value={city}
                    onChange={(e) => setCity(e.target.value)}
                    placeholder="Enter city"
                />
                <button onClick={handleFetchWeather}>Get Weather</button>
            </div>
            {weatherData && <WeatherCard weatherData={weatherData} city={city} />}
        </div>
    );
}

export default App;
