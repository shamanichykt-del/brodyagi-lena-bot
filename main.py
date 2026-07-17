from datetime import datetime
from config import TIMEZONE
import pytz


def test_bot():

    tz = pytz.timezone(TIMEZONE)

    now = datetime.now(tz)

    message = f"""
🌲 Бродяги | Гидросводка Лены

✅ Система запущена

Время:
{now.strftime("%d.%m.%Y %H:%M")}

Модули:
🌤 Погода — подготовка
🌊 Гидропосты — подготовка
🚁 FPV — подготовка
🎣 Рыбалка — подготовка
"""

    print(message)


if __name__ == "__main__":
    test_bot()
