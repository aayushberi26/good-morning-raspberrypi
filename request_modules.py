from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, LCD_FONT

from environment import (
    accuweather_url,
    accuweather_location_code,
    accuweather_access_key,
)
from modules import (
    weather,
    birthday,
    birthday_output
)

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=32, height=8, block_orientation=-90)

def display_data():
    msg = ''
    weather_response = weather.request_weather(accuweather_url, accuweather_location_code, accuweather_access_key)
    if weather_response:
        msg += weather_response + ', '
        # birthdays previously stored because the request takes a long time
        msg += birthday_output.birthdays
    show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.020)
