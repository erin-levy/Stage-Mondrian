from pyglet import shapes
from random import randrange


class Carrés:
    def __init__(self, width, height):
        self.quadrillage = []
        x = 0
        y = 0
        while x < width or y < height:
            largeur = randrange(width)
            longueur = 100
            self.quadrillage.append(
                shapes.BorderedRectangle(
                    x, y, largeur, longueur, 5, border_color=(0, 0, 0)
                )
            )
            if x >= width:
                x = 0
                y += longueur
            else:
                x += largeur

    def draw(self):
        for carré in self.quadrillage:
            carré.draw()
