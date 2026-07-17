import requests
from config import OPENWEATHER_API_KEY


def get_weather(city):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "ru"
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    data = response.json()

    if response.status_code != 200:
        return f"Ошибка погоды: {data.get('message')}"

    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]

    wind = data["wind"]["speed"]

    description = data["weather"][0]["description"]

    return f"""
🌤 {city}

🌡 Температура:
{temp:.0f}°C

Ощущается:
{feels:.0f}°C

☁️ {description}

💨 Ветер:
{wind} м/с

💧 Влажность:
{humidity}%

📈 Давление:
{pressure} гПа
"""


if __name__ == "__main__":

    print(get_weather("Yakutsk"))
