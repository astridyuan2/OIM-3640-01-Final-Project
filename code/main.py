from weatherapi import fetch_forecast, fetch_historical
from weather_interpretation import interpret_trip_weather
from packing_list import generate_trip_packing_list
from datetime import datetime, timedelta

def main():
    city = input("Enter destination city: ").strip()
    country_code = (input("Enter country code (default 'us'): ").strip() or "us").lower()
    duration = int(input("Enter travel duration in days: ").strip())
    start_date_str = input("Enter start date (YYYY-MM-DD): ").strip()
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = start_date + timedelta(days=duration)

    # Decide forecast vs historical
    today = datetime.today()
    forecast_limit = today + timedelta(days=7)

    if start_date <= forecast_limit:
        weather_list = fetch_forecast(city, country_code, start_date, end_date)
        is_historical = False
    else:
        weather_list = fetch_historical(city, country_code, start_date, end_date)
        is_historical = True

    print(f"\nWeather outlook for {city} ({start_date.date()} to {end_date.date()}):")
    print(interpret_trip_weather(weather_list, is_historical=is_historical))

    packing_list = generate_trip_packing_list(weather_list)
    print("\nRecommended Packing List:")
    for item in packing_list:
        print(f"- {item}")

if __name__ == "__main__":
    main()
