from random import randrange, choice
from pyglet import shapes
import numpy as np


class Couleurs3:
    def __init__(self, coord_x, dico_rencontre):

        carrés_formés = []

        self.quadrillage = []

        rouge = (230, 0, 0)
        bleu = (0, 0, 200)
        jaune = (250, 235, 0)
        gris = (220, 217, 207)
        noir = (59, 57, 50)
        blanc = (250, 250, 250)

        couple_x_x = {}

        u = 1
        for i1 in range(len(coord_x) - 1):
            y_sim = [[-1, 0]]
            x1 = coord_x[i1]
            couple_x_x[x1] = {}
            for i2 in range(u, len(coord_x)):

                x2 = coord_x[i2]

                if i1 != 0 or i2 != len(coord_x) - 1:
                    x1_x2_y_commun = []

                    for y in dico_rencontre[x1]:
                        if y in dico_rencontre[x2]:
                            x1_x2_y_commun.append(y)

                        if len(x1_x2_y_commun) >= 2:
                            couple_y_y = []

                            for i in range(len(x1_x2_y_commun) - 1):
                                for n in range(len(y_sim)):
                                    if (
                                        y_sim[n][0] != x1_x2_y_commun[i]
                                        or y_sim[n][1] >= x1_x2_y_commun[i + 1]
                                    ):

                                        couple_y_y.append(
                                            [x1_x2_y_commun[i], x1_x2_y_commun[i + 1]]
                                        )
                                        y_sim.append(
                                            [x1_x2_y_commun[i], x1_x2_y_commun[i + 1]]
                                        )

                            for i in range(len(x1_x2_y_commun) - 2):
                                for n in range(len(y_sim)):
                                    if (
                                        y_sim[n][0] != x1_x2_y_commun[i]
                                        or y_sim[n][1] >= x1_x2_y_commun[i + 2]
                                    ):
                                        couple_y_y.append(
                                            [x1_x2_y_commun[i], x1_x2_y_commun[i + 2]]
                                        )
                                        y_sim.append(
                                            [x1_x2_y_commun[i], x1_x2_y_commun[i + 2]]
                                        )

                            couple_x_x[x1][x2] = couple_y_y
                        else:
                            couple_x_x[x1][x2] = []
            u += 1

        print("dico carré : ", couple_x_x)
        nombre_carrés_possible = 0
        for x1 in couple_x_x:
            for x2 in couple_x_x[x1]:
                nombre_carrés_possible += len(couple_x_x[x1][x2])

        nbr_carrés = randrange(nombre_carrés_possible)

        for coul in range(5):

            indice_x1 = randrange(len(coord_x) - 1)
            if indice_x1 == 0:
                indice_x2 = randrange(indice_x1 + 1, len(coord_x) - 1)
            else:
                indice_x2 = randrange(indice_x1 + 1, len(coord_x))

            x_1 = coord_x[indice_x1]
            x_2 = coord_x[indice_x2]

            liste_couple_y = couple_x_x[x_1][x_2]
            if liste_couple_y != []:
                couple_y = choice(liste_couple_y)

                y_1 = couple_y[0]
                y_2 = couple_y[1]

                couple_x_x[x_1][x_2].remove(couple_y)
                if len(couple_x_x[x_1][x_2]) == 0:
                    del couple_x_x[x_1][x_2]

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

                self.quadrillage.append(
                    shapes.Rectangle(x_1, y_1, x_2 - x_1, y_2 - y_1, color=couleur)
                )
                carrés_formés.append([x_1, x_2, y_1, y_2, couleur])

    def draw(self):
        for carré in self.quadrillage:
            carré.draw()
