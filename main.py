import os
import pyxel

os.path.isfile('./constants.py')
import constants
from humans import Humans, Infected


class App:
    def __init__(self):

        # 1. Инициализируем приложение
        pyxel.init(constants.WIDTH, constants.HEIGHT)

        # 2. Создаём
        self.humans = Humans()
        self.infected = Infected()

        # 3. Запускаем приложение
        pyxel.run(self.update, self.draw)

    def update(self):
        """ Обновляем """

        # 1. Обновляем
        self.humans.update()
        self.infected.update()

        # 2. Заражаем
        for infected in self.infected.list:
            for human in self.humans.list:
                if infected.x == human.x and infected.y == human.y:
                    human.color = pyxel.COLOR_RED
                    self.infected.list.append(human)
                    self.humans.list.remove(human)
                    break

    def draw(self):
        """ Рисуем """

        # 1. Очищаем экран
        pyxel.cls(constants.COLOR_BACKGROUND)

        # 2. Рисуем
        self.humans.draw()
        self.infected.draw()

        # 3. Рисуем количество заражённых
        pyxel.text(1, 1, f'Infected: {len(self.infected.list)}', constants.COLOR_TEXT)


App()
