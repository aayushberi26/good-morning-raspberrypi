import re
import time

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

from environment import (
    accuweather_url,
    accuweather_location_code,
    accuweather_access_key,
    zip_code,
    facebook_birthday_url,
)
from modules import (
    weather,
    birthday
)

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=32, height=8, block_orientation=-90)

if __name__ == '__main__':
    weather = weather.request_weather(accuweather_url, accuweather_location_code, accuweather_access_key)
    if weather_response:
        msg = weather_response
    msg += birthday.request_birthdays(facebook_birthday_url)
    show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.028)
