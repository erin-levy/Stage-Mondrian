from random import randrange
from pyglet import shapes


class Grille:
    def __init__(self, width, height):

        x_deb = randrange(50, width - 50)

        self.hori = []
        self.verti = []

        for y in range(randrange(5, 10)):
            self.hori.append(randrange(height))

        for x in range(randrange(5, 10)):
            self.verti.append(randrange(width))

        self.quadrillage = [
            shapes.Line(x_deb, 0, x_deb, height, width=7, color=(0, 0, 0))
        ]

        for y in self.hori:
            x_1 = self.verti[randrange(len(self.verti))]
            x_2 = self.verti[randrange(len(self.verti))]
            self.quadrillage.append(
                shapes.Line((x_1 + 7), y, (x_2 + 7), y, width=7, color=(0, 0, 0))
            )

        for x in self.verti:
            y_1 = self.hori[randrange(len(self.hori))]
            y_2 = self.hori[randrange(len(self.hori))]
            self.quadrillage.append(
                shapes.Line(x, (y_1 + 7), x, (y_2 + 7), width=7, color=(0, 0, 0))
            )

    def draw(self):
        for lignes in self.quadrillage:
            lignes.draw()
