# # packing_logic.py

# from typing import List, Dict

# def generate_packing_list(
#     day_summaries: List[dict],
#     activities: List[str]
# ) -> Dict[str, Dict[str, int]]:
#     """
#     Generate a packing list.

#     Returns something like:
#     {
#       "Clothing": {"t-shirts": 5, "jeans": 2, "socks": 7, ...},
#       "Footwear": {"sneakers": 1, "hiking_boots": 1},
#       "Hygiene": {"toothbrush": 1, "toothpaste": 1},
#       "Electronics": {"phone_charger": 1, "travel_adapter": 1},
#       "Optional": {"umbrella": 1, "swimsuit": 1}
#     }
#     """
#     ...

# def suggest_outfits(day_summaries: List[dict], activities: List[str]) -> List[dict]:
#     """
#     (Stretch) Suggest daily outfits.

#     Returns:
#       [
#         {"date": "2025-12-10",
#          "description": "Cold rainy hiking outfit",
#          "items": ["thermal base layer", "fleece", "waterproof shell", ...]},
#         ...
#       ]
#     """
#     ...





from math import ceil
from typing import List, Dict

def generate_packing_list(day_summaries: List[dict], activities: List[str]) -> Dict[str, Dict[str, int]]:
    days = len(day_summaries)

    # baseline clothes
    shirts = ceil(days / 2)
    pants = max(1, ceil(days / 3))
    underwear = days
    socks = days

    # climate adjustments
    any_cold = any(d["temp_category"] == "cold" for d in day_summaries)
    any_rainy = any(d["precip_category"] == "rainy" for d in day_summaries)

    outerwear = 1 if any_cold else 0
    rain_jacket = 1 if any_rainy else 0

    footwear = {"sneakers": 1}
    if "hiking" in activities:
        footwear["hiking_boots"] = 1
    if "beach" in activities:
        footwear["sandals"] = 1

    clothing = {
        "t-shirts": shirts,
        "pants": pants,
        "underwear": underwear,
        "socks": socks,
    }
    if outerwear:
        clothing["warm_jacket"] = outerwear
    if rain_jacket:
        clothing["rain_jacket"] = rain_jacket
    if "beach" in activities:
        clothing["swimsuit"] = 1

    hygiene = {
        "toothbrush": 1,
        "toothpaste": 1,
        "deodorant": 1,
    }

    electronics = {
        "phone": 1,
        "phone_charger": 1,
        "travel_adapter": 1,
        "power_bank": 1,
    }

    optional = {}
    if any_rainy:
        optional["umbrella"] = 1

    return {
        "Clothing": clothing,
        "Footwear": footwear,
        "Hygiene": hygiene,
        "Electronics": electronics,
        "Optional": optional,
    }
