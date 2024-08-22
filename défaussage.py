marge = 1 / 12 * min(self.width, self.height)

        traits_max_x = (self.width // (2 * marge - 1)) + 1
        traits_max_y = (self.height // (2 * marge - 1)) + 1

        nbr_x = randrange(2, min(traits_max_x, traits_max_y))

        nbr_y = randrange(nbr_x - 1, min(nbr_x + (randrange(7)), traits_max_y))

        coord_x = liste_coord(x, width, nbr_x, marge)

        coord_y = liste_coord(y, height, nbr_y, marge)

        self.rencontre = créa_dico(coord_x)
        initialisation_dico(self.rencontre, x, y, width, height)

        self.dico_x = créa_dico(coord_x)
        initialisation_dico(self.dico_x, x, y, width, height)

        self.dico_y = créa_dico(coord_y)
        initialisation_dico(self.dico_y, y, x, height, width)

        self.possibilités_début_y = {}
        self.ou_il_faut_passer = {}
        for y in coord_y[2:]:
            self.possibilités_début_y[y] = list(coord_x)
            self.ou_il_faut_passer[y] = []

        # faire toutes les colonnes aléatoirement
        place_prise_par_colonnes = [height, 0]
        place_prise_par_lignes = [width, 0]

        for i in range(len(coord_x) - 2):

            debut = choice(coord_y)

            fin = choice(coord_y)

            while debut == fin:
                fin = choice(coord_y)

            place_prise_par_colonnes[0] = min(place_prise_par_colonnes[0], debut, fin)
            place_prise_par_colonnes[1] = max(place_prise_par_colonnes[1], debut, fin)

            self.dico_x[coord_x[i + 2]].append(debut)
            self.dico_x[coord_x[i + 2]].append(fin)

            if debut == 0 or debut == height:
                self.rencontre[coord_x[i + 2]].append(debut)
            else:
                self.possibilités_début_y[debut].remove(coord_x[i + 2])
                self.ou_il_faut_passer[debut].append(coord_x[i + 2])

            if fin == 0 or fin == height:
                self.rencontre[coord_x[i + 2]].append(fin)
            else:
                self.possibilités_début_y[fin].remove(coord_x[i + 2])
                self.ou_il_faut_passer[fin].append(coord_x[i + 2])

            for y in self.possibilités_début_y:
                if (fin < y and debut < y) or (fin > y and debut > y):
                    self.possibilités_début_y[y].remove(coord_x[i + 2])

        # essayer que toutes les colonnes fassent toute la longueur de l'écran

        pas_de_barre(
            coord_x,
            self.rencontre,
            self.dico_x,
            place_prise_par_colonnes,
            width,
            height,
            marge,
        )

        for y in self.possibilités_début_y:
            self.possibilités_début_y[y].sort()

            if self.ou_il_faut_passer[y] != []:

                i_min = 1
                while self.possibilités_début_y[y][i_min] < min(
                    self.ou_il_faut_passer[y]
                ):
                    i_min += 1

                i_max = 0
                while self.possibilités_début_y[y][i_max] < max(
                    self.ou_il_faut_passer[y]
                ):
                    i_max += 1

                debut = self.possibilités_début_y[y][randrange(i_min)]

                fin = self.possibilités_début_y[y][
                    randrange(i_max, len(self.possibilités_début_y[y]))
                ]

            else:
                debut = choice(self.possibilités_début_y[y])

                fin = choice(self.possibilités_début_y[y])

            self.dico_y[y].append(debut)
            self.dico_y[y].append(fin)

            place_prise_par_lignes[0] = min(place_prise_par_lignes[0], debut, fin)
            place_prise_par_lignes[1] = max(place_prise_par_lignes[1], debut, fin)

            for x in coord_x:
                if (
                    self.dico_x[x][0] <= y <= self.dico_x[x][1]
                    or self.dico_x[x][0] >= y >= self.dico_x[x][1]
                ) and (
                    debut == x or fin == x or (fin < x < debut) or (debut < x < fin)
                ):
                    self.rencontre[x].append(y)
                    self.rencontre[x].sort()

        pas_de_barre(
            coord_y,
            self.rencontre,
            self.dico_y,
            place_prise_par_lignes,
            height,
            width,
            marge,
        )
