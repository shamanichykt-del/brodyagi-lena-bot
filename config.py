import os
from dotenv import load_dotenv

load_dotenv()

MAX_TOKEN = os.getenv("MAX_TOKEN")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
CHANNEL_ID = os.getenv("CHANNEL_ID")

TIMEZONE = os.getenv(
    "TIMEZONE",
    "Asia/Yakutsk"
)
