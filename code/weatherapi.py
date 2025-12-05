import json
import os
import urllib.request
import urllib.parse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
APIKEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city, country_code="us", units="imperial"):
    """
    Fetch current weather data for a given city using OpenWeatherMap API.
    
    Args:
        city (str): City name (e.g., "New York", "São Paulo").
        country_code (str): Country code (default: 'us').
        units (str): 'imperial' for °F, 'metric' for °C, 'standard' for Kelvin.
    
    Returns:
        dict: Parsed weather data including temperature, humidity, description.
    """
    if not APIKEY:
        raise ValueError("Missing OpenWeatherMap API key. Set OPENWEATHER_API_KEY in your .env file.")

    # Build query with proper URL encoding
    query = {
        "q": f"{city},{country_code}".strip(),
        "APPID": APIKEY,
        "units": units
    }
    url = f"{BASE_URL}?{urllib.parse.urlencode(query)}"

    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read().decode("utf-8")
            weather_data = json.loads(response_text)
    except Exception as e:
        raise RuntimeError(f"Failed to fetch weather data: {e}")

    # Basic API error handling (e.g., city not found)
    if str(weather_data.get("cod")) != "200":
        message = weather_data.get("message", "Unknown error")
        raise ValueError(f"API error (cod={weather_data.get('cod')}): {message}")

    return {
        "city": weather_data["name"],
        "temperature": weather_data["main"]["temp"],
        "humidity": weather_data["main"]["humidity"],
        "description": weather_data["weather"][0]["description"]
    }

def main():
    city = input("Enter a city name: ").strip()
    country_code = (input("Enter country code (default 'us'): ").strip() or "us").lower()

    try:
        weather = fetch_weather(city, country_code=country_code, units="imperial")
        print(f"\nWeather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°F")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Conditions: {weather['description']}")
    except Exception as e:
        print(f"[error] {e}")

if __name__ == "__main__":
    main()
