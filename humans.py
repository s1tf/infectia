import os
import pyxel
import random

os.path.isfile('./constants.py')
import constants


class Humans(object):
    def __init__(self):
        """ Люди """

        # 1. Список
        self.list = [Human() for i in range(constants.HUMANS_TOTAL-1)]

    def update(self):
        """ Обновляем """

        # 1. Обновляем
        [i.update() for i in self.list]

    def draw(self):
        """ Рисуем """

        # 1. Рисуем
        [i.draw() for i in self.list]


class Infected(object):
    def __init__(self):
        """ Инфицированные """

        # 1. Список
        self.list = [Human(constants.COLOR_INFECTED)]

    def update(self):
        """ Обновляем """

        # 1. Обновляем
        [i.update() for i in self.list]

    def draw(self):
        """ Рисуем """

        # 1. Рисуем
        [i.draw() for i in self.list]


class Human(object):
    def __init__(self, color=constants.COLOR_HUMAN):
        """ Человек """

        # 1. Координаты
        self.x = random.randint(0, pyxel.width)
        self.y = random.randint(0, pyxel.height)

        # 2. Цвет
        self.color = color

    def update(self):
        """ Обновляем """

        # 1. Обновляем координаты
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

        if self.x < 0:
            self.x = 0
        elif self.x > pyxel.width:
            self.x = pyxel.width

        if self.y < 0:
            self.y = 0
        elif self.y > pyxel.height:
            self.y = pyxel.height

    def draw(self):
        """ Рисуем """

        # 1. Рисуем
        pyxel.pset(self.x, self.y, self.color)
