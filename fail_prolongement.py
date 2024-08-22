def prolongement(self):
    if min(self.dico_x) > -20:
        nouv_I = init(min(self.dico_x) - self.width, 0, self.width, self.height)

        self.dico_x |= nouv_I["dico_x"]
        self.dico_y |= nouv_I["dico_y"]

    if max(self.dico_x) < self.width + 20:
        nouv_I = init(max(self.dico_x), 0, self.width, self.height)

        self.dico_x |= nouv_I["dico_x"]
        self.dico_y |= nouv_I["dico_y"]

    if min(self.dico_y) > -20:
        nouv_I = init(0, min(self.dico_y) - self.height, self.width, self.height)

        self.dico_x |= nouv_I["dico_x"]
        self.dico_y |= nouv_I["dico_y"]

    if max(self.dico_y) < self.height + 20:
        nouv_I = init(0, max(self.dico_x), self.width, self.height)

        self.dico_x |= nouv_I["dico_x"]
        self.dico_y |= nouv_I["dico_y"]






self.carré[1] -= 1
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
            print(self.bords)

            nouv_I = init(C[0], C[1], self.bords[(i, j)], self.width, self.height)

            self.dicos_x.append(nouv_I["dico_x"])

            self.dicos_y.append(nouv_I["dico_y"])

            self.bords = dico_bords(
                self.bords, i, j, self.dicos_x[-1], self.dicos_y[-1]
            )
            self.debut_x -= self.width