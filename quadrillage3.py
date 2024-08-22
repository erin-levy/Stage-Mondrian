from random import randrange
from pyglet import shapes


class Grille3:
    def __init__(self, width, height):

        self.lignes = []

        x = randrange(width)
        y = randrange(height)

        if randrange(2) == 0:
            a = 0
        else:
            a = x

        self.quadrillage = [
            shapes.Line(
                x,
                0,
                x,
                height,
                width=7,
                color=(0, 0, 0),
            ),
            shapes.Line(
                a,
                y,
                width,
                y,
                width=7,
                color=(0, 0, 0),
            ),
        ]

        for i in range(randrange(2, 10)):
            b = randrange(x, width)
            self.quadrillage.append(
                shapes.Line(
                    b,
                    0,
                    b,
                    y,
                    width=7,
                    color=(0, 0, 0),
                ),
            )

    def draw(self):
        for lignes in self.quadrillage:
            lignes.draw()
