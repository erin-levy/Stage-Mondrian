from pyglet import shapes
from fonctions_quadrillage4 import (
    zoom_quadrillage,
    déplacement_quadrillage,
    dico_bords,
    coord_nouv,
)
from init_quadrillage import init


class Grille4:
    def __init__(self, width, height):
        self.largeur_trait = 7

        self.width = width
        self.height = height

        I = init(0, 0, {}, self.width, self.height)

        self.debut_x = 0
        self.debut_y = 0
        self.fin_x = self.width
        self.fin_y = self.height

        self.rencontre = I["rencontre"]
        self.dicos_x = [I["dico_x"]]
        self.dicos_y = [I["dico_y"]]
        self.possibilités_début_y = I["possibilités_début_y"]
        self.ou_il_faut_passer = I["ou_il_faut_passer"]
        self.carré = [0, 0]
        self.bords = dico_bords(
            {}, self.carré[0], self.carré[1], self.dicos_x[-1], self.dicos_y[-1]
        )

        # print(self.dicos_x)
        # print(self.bords)
        # print(self.bords[(0, 1)])

    def déplacement(self, dx, dy):
        self.dicos_x = déplacement_quadrillage(self.dicos_x, dx, dy)

        self.dicos_y = déplacement_quadrillage(self.dicos_y, dy, dx)

        self.debut_x += dx
        self.debut_y += dy
        self.fin_x += dx
        self.fin_y += dy

    def zoom(self, x, y, grandissement):
        if grandissement != 0:
            self.width += grandissement * self.width
            self.height += grandissement * self.height

            self.debut_x += (self.debut_x - x) * grandissement
            self.debut_y += (self.debut_y - y) * grandissement
            self.fin_x += (self.fin_x - x) * grandissement
            self.fin_y += (self.fin_y - y) * grandissement

            self.largeur_trait *= 1 + grandissement

            self.dicos_x = zoom_quadrillage(
                x,
                y,
                self.dicos_x,
                grandissement,
            )
            self.dicos_y = zoom_quadrillage(
                y,
                x,
                self.dicos_y,
                grandissement,
            )

    def prolongement(self):
        if self.debut_x >= 0:

            self.carré[0] -= 1
            i = self.carré[0]
            j = self.carré[1]

            C = coord_nouv(
                i,
                j,
                self.debut_x,
                self.debut_y,
                self.width,
                self.height,
            )
            # print(self.bords[(i, j)])
            nouv_I = init(C[0], C[1], self.bords[(i, j)], self.width, self.height)

            self.dicos_x.append(nouv_I["dico_x"])

            self.dicos_y.append(nouv_I["dico_y"])

            self.bords = dico_bords(
                self.bords, i, j, self.dicos_x[-1], self.dicos_y[-1]
            )
            self.debut_x -= self.width

        if self.debut_y >= 0:
            pass

    def draw(self):
        for i in range(len(self.dicos_x)):
            for x in self.dicos_x[i]:
                if len(self.dicos_x[i][x]) != 3:
                    shapes.Line(
                        x,
                        self.dicos_x[i][x][0],
                        x,
                        self.dicos_x[i][x][1],
                        width=self.largeur_trait,
                        color=(0, 0, 0),
                    ).draw()
        for i in range(len(self.dicos_y)):
            for y in self.dicos_y[i]:
                if len(self.dicos_y[i][y]) != 3:
                    shapes.Line(
                        self.dicos_y[i][y][0],
                        y,
                        self.dicos_y[i][y][1],
                        y,
                        width=self.largeur_trait,
                        color=(0, 0, 0),
                    ).draw()
