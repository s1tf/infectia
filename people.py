import os
import pyxel
import random

os.path.isfile('./constants.py')
import constants


class People(object):
    def __init__(self):
        """ Обычные / Заражённые / Вылеченные люди """

        # 1. Список
        self.list = []

    def update(self):
        """ Обновляем """

        # 1. Обновляем
        [i.update() for i in self.list]

    def draw(self):
        """ Рисуем """

        # 1. Рисуем
        [i.draw() for i in self.list]


class Person(object):
    def __init__(self, image_u=0):
        """ Человек
        :param image_u: [опционально] координата U картинки
        """

        # 1. Загружаем рисунок
        self.image_u = image_u
        self.image = pyxel.Image(constants.IMAGE_PERSON['w'], constants.IMAGE_PERSON['h'])
        self.image.load(x=0, y=0, filename=constants.IMAGE_PERSON['file'])

        # 2. Координаты
        self.x = random.randint(0, pyxel.width-5)
        self.y = random.randint(0, pyxel.height-constants.STATUS_BAR_HEIGHT-constants.IMAGE_PERSON['h'])

    def update(self):
        """ Обновляем """

        # 1. Обновляем координаты
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

        if self.x < 0:
            self.x = 0
        elif self.x > pyxel.width-5:
            self.x = pyxel.width-5

        if self.y < 0:
            self.y = 0
        elif self.y > pyxel.height-constants.STATUS_BAR_HEIGHT-constants.IMAGE_PERSON['h']:
            self.y = pyxel.height-constants.STATUS_BAR_HEIGHT-constants.IMAGE_PERSON['h']

    def draw(self):
        """ Рисуем """

        # 1. Рисуем
        pyxel.blt(x=self.x, y=self.y, img=self.image, u=self.image_u, v=0, w=5, h=constants.IMAGE_PERSON['h'], colkey=constants.IMAGE_PERSON['colkey'])
