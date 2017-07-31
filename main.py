import re
import time

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

from environment import (
    openweather_key,
    openweather_url,
    zip_code
)
from modules import (
    weather
)

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=32, height=8, block_orientation=-90)

if __name__ == '__main__':
    msg = weather.request_weather(openweather_url, openweather_key, zip_code)
    show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.045)