from random import randrange, choice
from pyglet import shapes


class Grille4bis:
    def __init__(self, width, height):

        self.quadrillage = []

        self.nbr_x = randrange(6, 21)
        self.nbr_y = randrange(6, 21)
        marge = 50

        self.coord_y = [0, height]
        for i in range(self.nbr_x):
            trop_près = 1
            garde_fou = 0
            while trop_près != 0 and garde_fou <= 50:
                y_nouv = randrange(marge, height - marge)
                trop_près = 0
                for x_deja_la in self.coord_y:
                    if abs(y_nouv - x_deja_la) < marge:
                        trop_près += 1
                garde_fou += 1

            self.coord_y.append(y_nouv)

        self.rencontre = {}
        for y in self.coord_y:
            self.rencontre[y] = []
        self.rencontre[0].append(0)
        self.rencontre[0].append(width)
        self.rencontre[height].append(0)
        self.rencontre[height].append(width)

        self.debut_fin_y = {}
        for y in self.coord_y:
            self.debut_fin_y[y] = []
        self.debut_fin_y[0].append(0)
        self.debut_fin_y[0].append(width)
        self.debut_fin_y[height].append(0)
        self.debut_fin_y[height].append(width)

        self.coord_x = [0, width]
        for i in range(self.nbr_y):
            trop_près = 1
            while trop_près != 0:
                x_nouv = randrange(marge, width - marge)
                trop_près = 0
                for y_deja_la in self.coord_x:
                    if abs(x_nouv - y_deja_la) < marge and x_nouv != y_deja_la:
                        trop_près += 1
            self.coord_x.append(x_nouv)

        possibilités_début_x = {}
        ou_il_faut_passer = {}
        for x in self.coord_x[2:]:
            possibilités_début_x[x] = list(self.coord_y)
            ou_il_faut_passer[x] = []

        # faire toutes les colonnes aléatoirement
        place_prise_par_lignes = [width, 0]

        for i in range(len(self.coord_y) - 2):

            debut = choice(self.coord_x)

            fin = choice(self.coord_x)

            while debut == fin:
                fin = choice(self.coord_x)

            place_prise_par_lignes[0] = min(place_prise_par_lignes[0], debut, fin)
            place_prise_par_lignes[1] = max(place_prise_par_lignes[1], debut, fin)

            self.debut_fin_y[self.coord_y[i + 2]].append(debut)
            self.debut_fin_y[self.coord_y[i + 2]].append(fin)

            if debut == 0 or debut == width:
                self.rencontre[self.coord_y[i + 2]].append(debut)
            else:
                possibilités_début_x[debut].remove(self.coord_y[i + 2])
                ou_il_faut_passer[debut].append(self.coord_y[i + 2])

            if fin == 0 or fin == width:
                self.rencontre[self.coord_y[i + 2]].append(fin)
            else:
                possibilités_début_x[fin].remove(self.coord_y[i + 2])
                ou_il_faut_passer[fin].append(self.coord_y[i + 2])

            for x in possibilités_début_x:
                if (fin < x and debut < x) or (fin > x and debut > x):
                    possibilités_début_x[x].remove(self.coord_y[i + 2])

        # essayer que toutes les colonnes fassent toute la longueur de l'écran

        if place_prise_par_lignes[0] != 0:
            x_encore_nouv = randrange(height)
            self.coord_y.append(x_encore_nouv)
            self.rencontre[x_encore_nouv] = [0, min(place_prise_par_lignes)]
            self.debut_fin_y[x_encore_nouv] = [0, min(place_prise_par_lignes)]

        if place_prise_par_lignes[1] != width:
            x_encore_nouv = randrange(height)
            self.coord_y.append(x_encore_nouv)
            self.rencontre[x_encore_nouv] = [max(place_prise_par_lignes), width]
            self.debut_fin_y[x_encore_nouv] = [max(place_prise_par_lignes), width]

        self.debut_fin_x = {}
        for x in self.coord_x:
            self.debut_fin_x[x] = []

        for x in possibilités_début_x:
            possibilités_début_x[x].sort()

            if ou_il_faut_passer[x] != []:
                if max(possibilités_début_x[x]) < min(ou_il_faut_passer[x]):
                    i_min = len(possibilités_début_x[x]) - 1
                    i_max = len(possibilités_début_x[x]) - 1
                else:
                    i_min = 1
                    while possibilités_début_x[x][i_min] < min(ou_il_faut_passer[x]):
                        i_min += 1

                    i_max = 0
                    while possibilités_début_x[x][i_max] < max(ou_il_faut_passer[x]):
                        i_max += 1

                debut = possibilités_début_x[x][randrange(i_min)]

                fin = possibilités_début_x[x][
                    randrange(i_max, len(possibilités_début_x[x]))
                ]
            else:
                debut = choice(possibilités_début_x[x])

                fin = choice(possibilités_début_x[x])

            self.debut_fin_x[x].append(debut)
            self.debut_fin_x[x].append(fin)

            for y in self.coord_y:
                if (
                    self.debut_fin_y[y][0] <= x <= self.debut_fin_y[y][1]
                    or self.debut_fin_y[y][0] >= x >= self.debut_fin_y[y][1]
                ) and (
                    debut == y or fin == y or (fin < y < debut) or (debut < y < fin)
                ):
                    self.rencontre[y].append(x)
                    self.rencontre[y].sort()

        del self.debut_fin_y[0]
        del self.debut_fin_y[height]
        del self.debut_fin_x[0]
        del self.debut_fin_x[width]

        self.coord_y.sort()
        self.coord_x.sort()

        # print("rencontre : ", self.rencontre)
        # print("coord x :", self.coord_x)
        # print("coord y :", self.coord_y)

    def draw(self):
        for x in self.debut_fin_x:
            self.quadrillage.append(
                shapes.Line(
                    x,
                    self.debut_fin_x[x][0],
                    x,
                    self.debut_fin_x[x][1],
                    width=7,
                    color=(0, 0, 0),
                ),
            )

        for y in self.debut_fin_y:
            self.quadrillage.append(
                shapes.Line(
                    self.debut_fin_y[y][0],
                    y,
                    self.debut_fin_y[y][1],
                    y,
                    width=7,
                    color=(0, 0, 0),
                ),
            )
        for lignes in self.quadrillage:
            lignes.draw()
