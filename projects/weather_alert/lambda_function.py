# lambda_function.py

import requests
import json
import os
from config import OPENWEATHER_API_KEY, LATITUDE, LONGITUDE

def get_current_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data["weather"][0]["main"]  # e.g. "Rain", "Clear", etc.

def load_last_weather(filename="last_weather.json"):
    if not os.path.exists(filename):
        return None
    with open(filename, "r") as f:
        return json.load(f).get("condition")

def save_current_weather(condition, filename="last_weather.json"):
    with open(filename, "w") as f:
        json.dump({"condition": condition}, f)

def main():
    current = get_current_weather()
    previous = load_last_weather()

    if previous is None:
        print(f"[INIT] Saving initial weather: {current}")
    elif current != previous:
        print(f"[ALERT] Weather changed from {previous} → {current}")
    else:
        print(f"[OK] Weather unchanged: {current}")

    save_current_weather(current)

if __name__ == "__main__":
    main()
