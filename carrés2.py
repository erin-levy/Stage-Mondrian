from pyglet import shapes
from random import randrange


class Carrés2:
    def __init__(self, width, height):
        aire = 0
        self.quadrillage = []

        x = randrange(50, width - 50)
        y = randrange(50, height - 50)
        largeur = randrange(50, width - x)
        longueur = randrange(50, height - y)

        aire = 0

        while aire < height * width:
            self.quadrillage.append(
                shapes.Line(
                    x,
                    y,
                    x + largeur,
                    y,
                    width=7,
                    color=(0, 0, 0),
                )
            )
            self.quadrillage.append(
                shapes.Line(
                    x,
                    y + longueur,
                    x,
                    y,
                    width=7,
                    color=(0, 0, 0),
                )
            )
            self.quadrillage.append(
                shapes.Line(
                    x,
                    y + longueur,
                    x + largeur,
                    y + longueur,
                    width=7,
                    color=(0, 0, 0),
                )
            )
            self.quadrillage.append(
                shapes.Line(
                    x + largeur,
                    y,
                    x + largeur,
                    y + longueur,
                    width=7,
                    color=(0, 0, 0),
                ),
            )

            aire += largeur * longueur

    def draw(self):
        for carré in self.quadrillage:
            carré.draw()
