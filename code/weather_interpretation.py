def interpret_weather(weather):
    """
    Turn raw weather data (from weatherapi.py) into a human-friendly interpretation.
    
    Args:
        weather (dict): Dictionary with keys like temperature, feels_like, humidity,
                        description, visibility, timezone, snow.
    
    Returns:
        str: A narrative interpretation of the weather.
    """
    temp_f = weather["temperature"]
    temp_c = round((temp_f - 32) * 5 / 9, 1)
    feels_f = weather["feels_like"]
    feels_c = round((feels_f - 32) * 5 / 9, 1) if feels_f is not None else None
    humidity = weather["humidity"]
    desc = weather["description"].capitalize()
    visibility = weather["visibility"]
    snow = weather["snow"]

    # Temperature interpretation
    if temp_f < 32:
        temp_msg = "It's freezing outside — bundle up!"
    elif temp_f < 50:
        temp_msg = "It's chilly, a jacket is recommended."
    elif temp_f < 70:
        temp_msg = "Mild and comfortable weather."
    elif temp_f < 85:
        temp_msg = "Warm weather, perfect for outdoor activities."
    else:
        temp_msg = "It's hot — stay hydrated and wear light clothing."

    # Humidity interpretation
    if humidity < 30:
        humidity_msg = "The air is dry."
    elif humidity < 60:
        humidity_msg = "Humidity feels comfortable."
    else:
        humidity_msg = "It feels humid and sticky."

    # Visibility interpretation
    if visibility is None:
        vis_msg = "Visibility data not available."
    elif visibility < 1000:
        vis_msg = "Visibility is poor — be cautious if traveling."
    elif visibility < 5000:
        vis_msg = "Visibility is moderate."
    else:
        vis_msg = "Visibility is clear."

    # Snow interpretation
    snow_msg = ""
    if snow is not None:
        snow_msg = f" Snowfall recorded: {snow} mm."

    # Feels like
    feels_msg = ""
    if feels_c is not None:
        feels_msg = f" It feels like {feels_f}°F / {feels_c}°C."

    return (
        f"{desc}. Temperature is {temp_f}°F / {temp_c}°C.{feels_msg} "
        f"{temp_msg} {humidity_msg} {vis_msg}{snow_msg}"
    )
