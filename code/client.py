# # cli.py

# def main() -> None:
#     """
#     Run the command-line interface for the AI Trip Packing Assistant.
#     """
#     print("=== AI Trip Packing Assistant ===")
#     # 1. Collect inputs
#     # 2. Fetch weather data
#     # 3. Interpret weather
#     # 4. Generate packing list
#     # 5. Pretty-print results


from .weather_api import fetch_weather
from .weather_interpretation import summarize_weather
from .packing_logic import generate_packing_list

def _prompt_activities() -> list:
    print("\nSelect activities for this trip (comma separated numbers):")
    print("1) City sightseeing")
    print("2) Hiking / outdoor")
    print("3) Business / formal")
    print("4) Sports / recreational")
    print("5) Beach / pool")
    choices = input("Your choice(s): ").strip()

    mapping = {
        "1": "city",
        "2": "hiking",
        "3": "business",
        "4": "sports",
        "5": "beach",
    }
    activities = []
    for c in choices.split(","):
        c = c.strip()
        if c in mapping:
            activities.append(mapping[c])
    return activities

def main() -> None:
    print("=== AI Trip Packing Assistant ===")
    location = input("Destination (e.g., Barcelona, London): ").strip()
    start_date = input("Start date (YYYY-MM-DD): ").strip()
    end_date = input("End date (YYYY-MM-DD): ").strip()

    activities = _prompt_activities()
    if not activities:
        print("No valid activities selected, defaulting to 'city'.")
        activities = ["city"]

    try:
        weather_data = fetch_weather(location, start_date, end_date)
    except ValueError as e:
        print(f"Error fetching weather: {e}")
        return

    summaries = summarize_weather(weather_data)
    packing_list = generate_packing_list(summaries, activities)

    print("\n=== Weather Summary ===")
    for d in summaries:
        print(f"{d['date']}: {d['temp_min']}–{d['temp_max']}°C, "
              f"{d['precip_prob']}% precip, {d['temp_category']} / {d['precip_category']}")

    print("\n=== Recommended Packing List ===")
    for category, items in packing_list.items():
        print(f"\n{category}:")
        for item, count in items.items():
            print(f"  - {item}: {count}")


from src.cli import main

if __name__ == "__main__":
    main()
