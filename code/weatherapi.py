# # weather_api.py

# def fetch_weather(location: str, start_date: str, end_date: str) -> dict:
#     """
#     Fetch weather data for a given location and date range.

#     Args:
#         location: City name or "City, Country".
#         start_date: 'YYYY-MM-DD'
#         end_date: 'YYYY-MM-DD'

#     Returns:
#         Dict containing cleaned weather data, e.g.
#         {
#             "dates": [...],
#             "max_temp": [...],
#             "min_temp": [...],
#             "precip_prob": [...]
#         }

#     Raises:
#         ValueError if location/date is invalid or API fails.
#     """
#     ...



import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"

def fetch_weather(location: str, start_date: str, end_date: str) -> dict:
    """
    For MVP: assume location is a city with known coordinates (hardcode a few examples)
    or you can add a simple dictionary mapping.

    For now, this function just demonstrates structure.
    """
    # TODO: replace with real geocoding or a mapping dict
    city_coords = {
        "Barcelona": (41.3851, 2.1734),
        "London": (51.5074, -0.1278),
        "Tenerife": (28.2916, -16.6291),
    }

    if location not in city_coords:
        raise ValueError(f"Unsupported location in MVP: {location}")

    lat, lon = city_coords[location]

    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": start_date,
        "end_date": end_date,
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_probability_max"],
        "timezone": "auto",
    }

    response = requests.get(BASE_URL, params=params, timeout=10)

    if response.status_code != 200:
        raise ValueError(f"Weather API error: {response.status_code}")

    data = response.json()
    daily = data.get("daily", {})

    return {
        "dates": daily.get("time", []),
        "max_temp": daily.get("temperature_2m_max", []),
        "min_temp": daily.get("temperature_2m_min", []),
        "precip_prob": daily.get("precipitation_probability_max", []),
    }




