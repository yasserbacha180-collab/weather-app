# Weather App
# Get real-time weather data for any city using OpenWeatherMap API

import urllib.request
import json

API_KEY = "your_api_key_here"  # Get a free key at https://openweathermap.org/api
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"City '{city}' not found. Please check the name.")
        elif e.code == 401:
            print("Invalid API key. Please check your key.")
        else:
            print(f"Error: {e.code}")
        return None
    except Exception as e:
        print(f"Connection error: {e}")
        return None

def display_weather(data, city):
    if not data:
        return

    name = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"].capitalize()
    wind_speed = data["wind"]["speed"]
    visibility = data.get("visibility", 0) // 1000

    print("\n" + "=" * 45)
    print(f"  Weather in {name}, {country}")
    print("=" * 45)
    print(f"  Condition    : {description}")
    print(f"  Temperature  : {temp}°C (feels like {feels_like}°C)")
    print(f"  Humidity     : {humidity}%")
    print(f"  Wind Speed   : {wind_speed} m/s")
    print(f"  Visibility   : {visibility} km")
    print("=" * 45)

def main():
    print("=" * 45)
    print("          Python Weather App")
    print("=" * 45)

    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()
        if city.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        if not city:
            print("Please enter a city name.")
            continue
        data = get_weather(city)
        display_weather(data, city)

if __name__ == "__main__":
    main()
