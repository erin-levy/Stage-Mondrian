from random import randrange, choice
from pyglet import shapes
import numpy as np


class Couleurs2:
    def __init__(self, coord_x, dico_rencontre):

        carrés_formés = []

        self.quadrillage = []

        rouge = (230, 0, 0)
        bleu = (0, 0, 200)
        jaune = (250, 235, 0)
        gris = (220, 217, 207)
        noir = (59, 57, 50)
        blanc = (250, 250, 250)

        couple_x_x = []
        y_commun_couple = []

        for i in range(len(coord_x) - 1):
            x1 = coord_x[i]
            x2 = coord_x[i + 1]

            x1_x2_y_commun = []

            for y in dico_rencontre[x1]:
                if y in dico_rencontre[x2]:
                    x1_x2_y_commun.append(y)

            if len(x1_x2_y_commun) >= 2:
                couple_y_y = []
                for i in range(len(x1_x2_y_commun) - 1):
                    couple_y_y.append([x1_x2_y_commun[i], x1_x2_y_commun[i + 1]])
                for i in range(len(x1_x2_y_commun) - 2):
                    couple_y_y.append([x1_x2_y_commun[i], x1_x2_y_commun[i + 2]])

                y_commun_couple.append(couple_y_y)
                couple_x_x.append([x1, x2])

        for i in range(len(coord_x) - 2):
            x1 = coord_x[i]
            x3 = coord_x[i + 2]

            x1_x3_y_commun = []

            for y in dico_rencontre[x1]:
                if y in dico_rencontre[x3]:
                    x1_x2_y_commun.append(y)

            if len(x1_x3_y_commun) >= 2:
                couple_y_y = []
                for i in range(len(x1_x3_y_commun) - 1):
                    couple_y_y.append([x1_x3_y_commun[i], x1_x3_y_commun[i + 1]])
                for i in range(len(x1_x2_y_commun) - 2):
                    couple_y_y.append([x1_x3_y_commun[i], x1_x3_y_commun[i + 2]])
                y_commun_couple.append(couple_y_y)
                couple_x_x.append([x1, x3])

        nombre_carrés_possible = 0
        for i in range(len(couple_x_x)):
            nombre_carrés_possible += len(y_commun_couple[i])

        nbr_carrés = randrange(nombre_carrés_possible // 2)
        # print(couple_x_x)

        for coul in range(nbr_carrés):

            indice_x = randrange(len(y_commun_couple))

            x_1 = couple_x_x[indice_x][0]
            x_2 = couple_x_x[indice_x][1]

            indice_y = randrange(len(y_commun_couple[indice_x]))

            y_1 = y_commun_couple[indice_x][indice_y][0]
            y_2 = y_commun_couple[indice_x][indice_y][1]

            del y_commun_couple[indice_x][indice_y]
            if y_commun_couple[indice_x] == []:
                del y_commun_couple[indice_x]
                del couple_x_x[indice_x]

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
                shapes.Rectangle(x_1, y_1, x_2 - x_1, y_2 - y_1, color=couleur)
            )
            carrés_formés.append([x_1, x_2, y_1, y_2, couleur])

    def draw(self):
        for carré in self.quadrillage:
            carré.draw()
