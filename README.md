# Weather App

A Python terminal app that shows real-time weather data for any city in the world using the OpenWeatherMap API.

## Features

- Search weather by city name
- Shows temperature, humidity, wind speed, visibility
- Feels-like temperature
- Works for any city worldwide
- Clean terminal output

## Setup

1. Get a free API key from [openweathermap.org](https://openweathermap.org/api)
2. Open `weather.py` and replace `your_api_key_here` with your key
3. Run the script:

```bash
python weather.py
```

## Example Output

```
=============================================
          Python Weather App
=============================================

Enter city name (or 'quit' to exit): Algiers

=============================================
  Weather in Algiers, DZ
=============================================
  Condition    : Clear sky
  Temperature  : 24.5°C (feels like 23.8°C)
  Humidity     : 58%
  Wind Speed   : 3.2 m/s
  Visibility   : 10 km
=============================================
```

## Technologies Used

- Python 3
- OpenWeatherMap API (free tier)
- `urllib` and `json` (standard library — no pip install needed)

## Author

**yasserbacha** — Computer Science Student
