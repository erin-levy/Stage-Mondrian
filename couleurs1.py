from random import randrange
from pyglet import shapes
import numpy as np


class Couleurs1:
    def __init__(self, width, coord_x, dico_rencontre):

        self.quadrillage = []

        rouge = (230, 0, 0)
        bleu = (0, 0, 200)
        jaune = (250, 235, 0)
        gris = (220, 217, 207)
        noir = (59, 57, 50)
        blanc = (250, 250, 250)

        y_commun = []
        x2 = width
        x1 = 0

        nbr_couleurs = randrange(15)
        for coul in range(1):
            while len(y_commun) < 2 or abs(x2 - x1) > (4 / 6) * width:
                x1 = coord_x[randrange(len(coord_x))]
                tempo = list(coord_x)
                tempo.remove(x1)

                x2 = tempo[randrange(len(tempo))]

                y_commun = []
                for y in dico_rencontre[x1]:
                    if y in dico_rencontre[x2]:
                        y_commun.append(y)

            y_commun.sort()

            i = randrange(len(y_commun))
            y1 = y_commun[i]
            if i < len(y_commun) - 2:
                y2 = y_commun[i + 1]
            if i == len(y_commun) - 2:
                y2 = y_commun[i + 1]
            if i > len(y_commun) - 2:
                y2 = y_commun[i - 1]

            couleur = blanc
            choix_couleur = np.random.binomial(4, 0.5)
            if choix_couleur == 3:
                couleur = rouge
            if choix_couleur == 1:
                couleur = bleu
            if choix_couleur == 2:
                couleur = jaune
            if choix_couleur == 4:
                couleur = gris
            if choix_couleur == 0:
                couleur = noir

            # print(x_1, x_2, y_1, y_2, couleur)

            self.quadrillage.append(
                shapes.Rectangle(x1, y1, x2 - x1, y2 - y1, color=couleur)
            )

    def draw(self):
        for carré in self.quadrillage:
            carré.draw()
