import os
import sys
import pyxel

# Разрешение экрана
WIDTH = 480  # _320 320 480 480
HEIGHT = 270  # 180 240 320 270

# Высота статус-бара
STATUS_BAR_HEIGHT = 15

# Количество людей
PEOPLE_TOTAL = 500

# Цвета
COLOR_BACKGROUND = 0
COLOR_PALE_PINK = 1
COLOR_RED = 2
COLOR_GREEN = 3

# Путь до файлов
try:
    PATH = sys._MEIPASS
except Exception:
    PATH = os.path.abspath('.')

# Изображения
IMAGE_PERSON = {'file': os.path.join(PATH, 'person.png'), 'w': 15, 'h': 13, 'colkey': pyxel.COLOR_BLACK}
IMAGE_BAR = {'file': os.path.join(PATH, 'bar.png'), 'w': 100, 'h': 10, 'colkey': pyxel.COLOR_WHITE}
