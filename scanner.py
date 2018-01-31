#!/usr/bin/python3
import pyscreenshot
import zbarlight

from screeninfo import get_monitors
from PIL import Image

file_path = '/tmp/screenshot.png'


def __get_screen_size():
    screen = get_monitors()[0]
    return [screen.width, screen.height]


def take_screenshot():
    screen = __get_screen_size()
    img = pyscreenshot.grab(bbox=(0, 0, screen[0], screen[1]))
    img.save(file_path)


if __name__ == '__main__':
    # task screen capture
    take_screenshot()
    # read qrcode
    with open(file_path, 'rb') as target:
        image = Image.open(file_path)
        image.load()

    result = zbarlight.scan_codes('qrcode', image)
    # echo result
    for index, item in enumerate(result):
        print('Qrcode -{}- | [{}]'.format(index, item))
