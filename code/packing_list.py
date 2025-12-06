
def generate_packing_list(weather):
    """
    Generate a packing list based on weather conditions.
    
    Args:
        weather (dict): Dictionary with keys like description, temperature, snow, humidity.
    
    Returns:
        list: Recommended items to pack.
    """
    items = []

    desc = weather["description"].lower()
    temp_f = weather["temperature"]
    snow = weather["snow"]

    # Rainy conditions
    if "rain" in desc:
        items.extend(["Waterproof jacket", "Umbrella", "Waterproof shoes"])

    # Snowy conditions
    if "snow" in desc or snow is not None:
        items.extend(["Puffer jacket", "Gloves", "Warm hat", "Snow boots"])

    # Cold weather
    if temp_f < 40:
        items.extend(["Heavy coat", "Scarf", "Thermal layers"])

    # Mild weather
    elif 40 <= temp_f < 70:
        items.extend(["Light jacket", "Comfortable shoes"])

    # Hot weather
    elif temp_f >= 85:
        items.extend(["Light clothing", "Sunglasses", "Hat", "Reusable water bottle"])

    # General essentials
    items.append("Daily essentials (phone, charger, ID, wallet)")

    return items


def main():
    from weatherapi import fetch_weather

    city = input("Enter a city name: ").strip()
    country_code = (input("Enter country code (default 'us'): ").strip() or "us").lower()

    try:
        weather = fetch_weather(city, country_code=country_code, units="imperial")
        packing_list = generate_packing_list(weather)

        print(f"\nPacking list for {weather['city']} based on current weather:")
        for item in packing_list:
            print(f"- {item}")
    except Exception as e:
        print(f"[error] {e}")


if __name__ == "__main__":
    main()
