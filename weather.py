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

    response = requests.get(url, params=params)

    data = response.json()

    return data
