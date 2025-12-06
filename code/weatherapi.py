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
        dict: Parsed weather data including temperature, feels_like, humidity,
              description, visibility, timezone, and snow volume if available.
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

    # Extract optional fields safely
    feels_like = weather_data["main"].get("feels_like")
    visibility = weather_data.get("visibility")  # in meters
    timezone = weather_data.get("timezone")      # shift in seconds from UTC
    snow = None
    if "snow" in weather_data:
        # API may provide "snow": {"1h": value, "3h": value}
        snow = weather_data["snow"].get("1h") or weather_data["snow"].get("3h")

    return {
        "city": weather_data["name"],
        "temperature": weather_data["main"]["temp"],
        "feels_like": feels_like,
        "humidity": weather_data["main"]["humidity"],
        "description": weather_data["weather"][0]["description"],
        "visibility": visibility,
        "timezone": timezone,
        "snow": snow
    }

def main():
    city = input("Enter a city name: ").strip()
    country_code = (input("Enter country code (default 'us'): ").strip() or "us").lower()

    try:
        # Fetch in Fahrenheit
        weather = fetch_weather(city, country_code=country_code, units="imperial")
        temp_f = weather["temperature"]
        temp_c = round((temp_f - 32) * 5 / 9, 1)

        feels_f = weather["feels_like"]
        feels_c = round((feels_f - 32) * 5 / 9, 1) if feels_f is not None else None

        # Convert timezone offset (seconds) into UTC±hours
        tz_offset = weather["timezone"]
        tz_hours = tz_offset // 3600 if tz_offset is not None else None

        print(f"\nWeather in {weather['city']}:")
        print(f"Temperature: {temp_f}°F / {temp_c}°C")
        if feels_c is not None:
            print(f"Feels like: {feels_f}°F / {feels_c}°C")
        else:
            print("Feels like: N/A")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Conditions: {weather['description']}")
        print(f"Visibility: {weather['visibility']} meters" if weather['visibility'] is not None else "Visibility: N/A")
        if tz_hours is not None:
            print(f"Timezone: UTC{tz_hours:+d}")
        else:
            print("Timezone: N/A")
        if weather["snow"] is not None:
            print(f"Snow volume: {weather['snow']} mm")
        else:
            print("Snow volume: N/A")
    except Exception as e:
        print(f"[error] {e}")


if __name__ == "__main__":
    main()
