import os
import pyxel

os.path.isfile('./constants.py')
os.path.isfile('./people.py')
import constants
from people import Person, People


class App:
    def __init__(self):

        # 1. Инициализируем приложение
        pyxel.init(constants.WIDTH, constants.HEIGHT)
        pyxel.mouse(visible=True)

        # 2. Меняем цвета на пользовательские
        pyxel.colors[constants.COLOR_PALE_PINK] = 0xffcc80  # телесный
        pyxel.colors[constants.COLOR_RED] = 0xe51c23  # красный
        pyxel.colors[constants.COLOR_GREEN] = 0x2baf2b  # зелёный

        # 3. Создаём людей
        self.people_normal = People()
        self.people_normal.list = [Person() for i in range(constants.PEOPLE_TOTAL - 1)]
        self.people_infected = People()
        self.people_infected.list = [Person(image_u=10)]
        self.people_cured = People()

        # 4. Создаём статус бар
        self.bar = pyxel.Image(constants.IMAGE_BAR['w'], constants.IMAGE_BAR['h'])
        self.bar.load(x=0, y=0, filename=constants.IMAGE_BAR['file'])

        # 5. Запускаем приложение
        pyxel.run(self.update, self.draw)

    def update(self):
        """ Обновляем """

        # 1. Обновляем
        self.people_normal.update()
        self.people_infected.update()
        self.people_cured.update()

        # 2. Заражаем
        for infected in self.people_infected.list:
            for person in self.people_normal.list:
                if abs(infected.x - person.x) < 5 and abs(infected.y - person.y) < 10:
                    person.image_u = 10
                    self.people_infected.list.append(person)
                    self.people_normal.list.remove(person)
                    break

            # При клике на заражённого - вылечиваем
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and (abs(infected.x - pyxel.mouse_x) < 5 and abs(infected.y - pyxel.mouse_y) < 10):
                infected.image_u = 5
                self.people_cured.list.append(infected)
                self.people_infected.list.remove(infected)
                break

    def draw(self):
        """ Рисуем """

        # 1. Очищаем экран
        pyxel.cls(constants.COLOR_BACKGROUND)

        # 2. Рисуем людей
        self.people_normal.draw()
        self.people_infected.draw()
        self.people_cured.draw()

        # 3. Рисуем статус бар
        pyxel.rect(x=0, y=pyxel.height-constants.STATUS_BAR_HEIGHT, w=pyxel.width, h=constants.STATUS_BAR_HEIGHT, col=pyxel.COLOR_GRAY)

        # 3. Рисуем статус бар
        pyxel.blt(x=2, y=pyxel.height-14, img=self.bar, u=0, v=0, w=constants.IMAGE_BAR['w'], h=constants.IMAGE_BAR['h'], colkey=constants.IMAGE_BAR['colkey'])
        pyxel.text(44, pyxel.height-9, str(len(self.people_infected.list)), constants.COLOR_RED)
        pyxel.text(104, pyxel.height-9, str(len(self.people_cured.list)), constants.COLOR_RED)


App()
