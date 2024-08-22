from random import randrange
from pyglet import shapes


class Grille2:
    def __init__(self, width, height):

        self.lignes = []

        for i in range(randrange(1, 10)):
            x = randrange(width)
            y = randrange(height)
            self.lignes.append([x, y])

        self.quadrillage = []

        for i in range(len(self.lignes)):
            self.quadrillage.append(
                shapes.Line(
                    self.lignes[i][0],
                    0,
                    self.lignes[i][0],
                    height,
                    width=7,
                    color=(0, 0, 0),
                )
            )

            if self.lignes[i][1] % 3 == 0:
                self.quadrillage.append(
                    shapes.Line(
                        self.lignes[i][0],
                        self.lignes[i][1],
                        width,
                        self.lignes[i][1],
                        width=7,
                        color=(0, 0, 0),
                    )
                )

            if self.lignes[i][1] % 2 == 0:
                self.quadrillage.append(
                    shapes.Line(
                        0,
                        self.lignes[i][1],
                        self.lignes[i][0],
                        self.lignes[i][1],
                        width=7,
                        color=(0, 0, 0),
                    )
                )

    def draw(self):
        for lignes in self.quadrillage:
            lignes.draw()
