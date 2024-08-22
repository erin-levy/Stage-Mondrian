import pyglet
from pyglet import shapes
from pyglet.window import key
import time
import json

from quadrillage_1 import Grille
from carrés import Carrés
from quadrillage_2 import Grille2
from quadrillage3 import Grille3
from grille4 import Grille4
from carrés2 import Carrés2
from quadrillage4bis import Grille4bis
from couleurs1 import Couleurs1
from couleurs2 import Couleurs2
from couleurs3 import Couleurs3
from couleurs4 import Couleurs4


class Mondrian(pyglet.window.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Tableau Mondrian", resizable=True)

        self.width = width
        self.height = height

        self.dx = 0
        self.dy = 0

        self.grandissement = 0

        self.x = 0
        self.y = 0

        self.fond_blanc = shapes.Rectangle(
            0, 0, self.width, self.height, color=(241, 238, 218)
        )

        # self.grille = Grille(self.width, self.height)
        # self.carrés = Carrés(self.width, self.height)
        # self.grille2 = Grille2(self.width, self.height)
        # self.grille3 = Grille3(self.width, self.height)
        self.grille4 = Grille4(self.width, self.height)
        # self.carrés2 = Carrés2(self.width, self.height)
        # self.grille4bis = Grille4bis(self.width, self.height)
        # self.couleurs1 = Couleurs1(
        #    self.width, self.grille4.coord_x, self.grille4.rencontre
        # )
        # self.couleurs2 = Couleurs2(self.grille4.coord_x, self.grille4.rencontre)
        # self.couleurs3 = Couleurs3(self.grille4.coord_x, self.grille4.rencontre)
        self.couleurs4 = Couleurs4(
            self.grille4.dicos_x[-1],
            self.grille4.dicos_y[-1],
        )
        # print(self.grille4.bords)
        pyglet.clock.schedule_interval(self.update, 1 / 20)

    def update(self, dt):

        self.grille4.déplacement(self.dx, self.dy)

        self.couleurs4.déplacement(self.dx, self.dy)

        self.grille4.zoom(self.x, self.y, self.grandissement)

        self.couleurs4.zoom(self.x, self.y, self.grandissement)

        # self.grille4.prolongement()

        # print("dico_x: ", self.grille4.dico_x)
        # print("dico_y: ", self.grille4.dico_y)

    def on_key_press(self, symbol, modifiers):

        if symbol == key.ENTER:
            f = open("historique" + ".json", "w")
            json.dump(
                {
                    "dim_fen": {"width": self.width, "height": self.height},
                    "verti": self.grille4.dicos_x,
                    "hori": self.grille4.dicos_y,
                    "carrés": self.couleurs4.carrés,
                    "y possibles": self.grille4.possibilités_début_y,
                    "où il faut passer": self.grille4.ou_il_faut_passer,
                    "largeur_trait": self.grille4.largeur_trait,
                },
                f,
            )
            debut = time.time()
            self.grille4.__init__(self.width, self.height)
            self.couleurs4.__init__(self.grille4.dicos_x[-1], self.grille4.dicos_y[-1])
            fin = time.time()
            print("temps=", fin - debut)

        if symbol == key.G:
            name = input("Rentrez le nom du tableau : ")
            f = open(name + ".json", "w")
            json.dump(
                {
                    "dim_fen": {"width": self.width, "height": self.height},
                    "verti": self.grille4.dicos_x,
                    "hori": self.grille4.dicos_y,
                    "carrés": self.couleurs4.carrés,
                    "y possibles": self.grille4.possibilités_début_y,
                    "où il faut passer": self.grille4.ou_il_faut_passer,
                    "largeur_trait": self.grille4.largeur_trait,
                },
                f,
            )

        if symbol == key.R:
            name = input("entrez le nom du tableau dejà existant : ")

            f = open(name + ".json", "r")
            parametres = json.load(f)

            parametres_x = {
                int(float(cle)): valeur
                for cle, valeur in parametres["verti"][0].items()
            }
            parametres_y = {
                int(float(cle)): valeur for cle, valeur in parametres["hori"][0].items()
            }

            self.grille4.dicos_x = [parametres_x]
            self.grille4.dicos_y = [parametres_y]
            self.couleurs4.carrés = parametres["carrés"]
            self.grille4.largeur_trait = parametres["largeur_trait"]

        if symbol == key.C:
            self.couleurs4.__init__(self.grille4.dicos_x[-1], self.grille4.dicos_y[-1])

        delta = 50

        if symbol == key.UP:
            self.dy = -delta
        elif symbol == key.DOWN:
            self.dy = delta
        elif symbol == key.LEFT:
            self.dx = delta
        elif symbol == key.RIGHT:
            self.dx = -delta

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.dy = 0
        elif symbol == key.DOWN:
            self.dy = 0
        elif symbol == key.LEFT:
            self.dx = 0
        elif symbol == key.RIGHT:
            self.dx = 0

    def on_mouse_press(self, x, y, button, modifiers):
        self.x = x
        self.y = y

        delta = 1 / 20

        if button == 1:
            self.grandissement += delta
        if button == 4:
            self.grandissement -= delta

    def on_mouse_release(self, x, y, button, modifiers):
        self.grandissement = 0

    def on_draw(self):
        self.fond_blanc.draw()
        # self.couleurs1.draw()
        # self.couleurs2.draw()
        # self.couleurs3.draw()
        self.couleurs4.draw()
        # self.carrés.draw()
        # self.carrés2.draw()
        # self.grille.draw()
        # self.grille2.draw()
        # self.grille3.draw()
        self.grille4.draw()
        # self.grille4bis.draw()


mondrian = Mondrian(600, 700)

print(
    "Entrée: Générer un nouveau tableau \nG : Garder le tableau \nR : Restaurer un tableau déjà existant \nFlèches : Déplacer le tableau \nClic gauche : Zoom \nClic droit : Dézoom"
)

pyglet.app.run()
