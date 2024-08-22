from random import randrange, choice
from pyglet import shapes
from fonctions_couleurs4 import trouver_lignes


class Couleurs4:
    def __init__(self, dico_x, dico_y):

        width_tableau = max(dico_x) - min(dico_x)
        height_tableau = max(dico_y) - min(dico_y)

        rouge = (200, 0, 0)
        bleu = (0, 0, 180)
        jaune = (220, 215, 0)
        gris = (171, 164, 156)
        noir = (59, 57, 50)

        a_max_gris = 1 / 7
        a_max_noir = 1 / 8

        self.carrés = []

        nbr_points_max = len(dico_y) + len(dico_x) + 1

        nbr_points = randrange(nbr_points_max)

        for pt in range(nbr_points):

            coul_possibles = [rouge, bleu, jaune, noir, gris]

            x = randrange(int(min(dico_x)) + 1, int(max(dico_x)))
            y = randrange(int(min(dico_y)) + 1, int(max(dico_y)))

            if x in dico_x:
                x += 1

            if y in dico_y:
                y += 1

            couple_x = trouver_lignes(x, y, dico_x)

            x1 = couple_x[0]
            x2 = couple_x[1]

            couple_y = trouver_lignes(y, x, dico_y)

            y1 = couple_y[0]
            y2 = couple_y[1]

            carres_à_cote = 0

            for carré in self.carrés:
                if x1 == carré["x0"] and y1 == carré["y0"]:
                    coul_possibles = []
                    break

                elif (
                    (x1 >= carré["x0"] or x2 >= carré["x0"])
                    and (
                        x1 <= carré["x0"] + carré["largeur"]
                        or x2 <= carré["x0"] + carré["largeur"]
                    )
                ) and (
                    (y1 >= carré["y0"] or y2 >= carré["y0"])
                    and (
                        y1 <= carré["y0"] + carré["longueur"]
                        or y2 <= carré["y0"] + carré["longueur"]
                    )
                ):
                    carres_à_cote += 1

                    if carré["couleur"] in coul_possibles and carré["couleur"] != gris:
                        coul_possibles.remove(carré["couleur"])

                    if (
                        (
                            x1 == carré["x0"] + carré["largeur"]
                            and y1 == carré["y0"] + carré["longueur"]
                        )
                        or (x2 == carré["x0"] and y2 == carré["y0"])
                        or (x2 == carré["x0"] and y1 == carré["y0"] + carré["longueur"])
                        or (x1 == carré["x0"] + carré["largeur"] and y2 == carré["y0"])
                    ) and (noir in coul_possibles):
                        coul_possibles.remove(noir)

            if len(self.carrés) == 0:
                coul_possibles.remove(gris)

            if (
                (y2 - y1) * (x2 - x1) >= a_max_gris * height_tableau * width_tableau
            ) and (gris in coul_possibles):
                coul_possibles.remove(gris)

            if (
                (y2 - y1) * (x2 - x1) >= a_max_noir * height_tableau * width_tableau
                or carres_à_cote == 0
            ) and (noir in coul_possibles):
                coul_possibles.remove(noir)

            if len(coul_possibles) == 0:
                break

            # if (
            #   len(self.carrés) != 1
            #  or self.carrés[0]["couleur"] != rouge
            # or nbr_points != 2
            # ) and (noir in coul_possibles):
            #   coul_possibles.remove(noir)

            coul = choice(coul_possibles)

            self.carrés.append(
                {
                    "x0": x1,
                    "y0": y1,
                    "largeur": x2 - x1,
                    "longueur": y2 - y1,
                    "couleur": coul,
                }
            )

    def déplacement(self, dx, dy):
        for carré in self.carrés:
            carré["x0"] += dx
            carré["y0"] += dy

    def zoom(self, x, y, grandissement):
        for carré in self.carrés:
            carré["x0"] += (carré["x0"] - x) * grandissement
            carré["y0"] += (carré["y0"] - y) * grandissement
            carré["largeur"] += carré["largeur"] * grandissement
            carré["longueur"] += carré["longueur"] * grandissement

    def draw(self):
        for carré in self.carrés:
            shapes.Rectangle(
                carré["x0"],
                carré["y0"],
                carré["largeur"],
                carré["longueur"],
                carré["couleur"],
            ).draw()
