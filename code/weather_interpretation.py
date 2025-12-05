# weather_interpretation.py

# from typing import List, Dict

# def categorize_day(temp_min: float, temp_max: float, precip_prob: float) -> dict:
#     """
#     Categorize a single day into climate labels.
#     Returns: {"temp_category": "cold/mild/hot", "precip_category": "dry/rainy"}
#     """
#     ...

# def summarize_weather(weather_data: Dict) -> List[dict]:
#     """
#     Takes cleaned weather_data (from weather_api) and returns a per-day summary:
#     [
#       {
#         "date": "2025-12-10",
#         "temp_min": 5,
#         "temp_max": 11,
#         "precip_prob": 0.6,
#         "temp_category": "cold",
#         "precip_category": "rainy",
#       },
#       ...
#     ]
#     """
#     ...



from typing import Dict, List

def categorize_day(temp_min: float, temp_max: float, precip_prob: float) -> dict:
    # simple, tweak later
    if temp_max < 10:
        temp_category = "cold"
    elif temp_max < 22:
        temp_category = "mild"
    else:
        temp_category = "hot"

    precip_category = "rainy" if precip_prob >= 50 else "dry"

    return {
        "temp_category": temp_category,
        "precip_category": precip_category,
    }

def summarize_weather(weather_data: Dict) -> List[dict]:
    summaries = []
    for date, tmin, tmax, p in zip(
        weather_data["dates"],
        weather_data["min_temp"],
        weather_data["max_temp"],
        weather_data["precip_prob"],
    ):
        cat = categorize_day(tmin, tmax, p)
        summaries.append({
            "date": date,
            "temp_min": tmin,
            "temp_max": tmax,
            "precip_prob": p,
            **cat,
        })
    return summaries

