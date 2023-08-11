import pyxel

import constants

class App:
    def __init__(self):
        pyxel.init(constants.WIDTH, constants.HEIGHT)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 16, 16, 1)

App()
