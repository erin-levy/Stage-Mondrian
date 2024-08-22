from random import randrange, choice
from fonctions_init import liste_coord, créa_dico, initialisation_dico, pas_de_barre


def init(deb_x, deb_y, dic_pos, width, height):

    fin_x = deb_x + width
    fin_y = deb_y + height

    marge = 1 / 12 * min(width, height)

    traits_max_x = (width // (2 * marge - 1)) + 1
    traits_max_y = (height // (2 * marge - 1)) + 1

    nbr_x = randrange(2, min(traits_max_x, traits_max_y))

    nbr_y = randrange(nbr_x - 1, min(nbr_x + (randrange(7)), traits_max_y))

    coord_x = liste_coord(deb_x, fin_x, nbr_x, marge)

    if "deb_x" in dic_pos:
        coord_x += dic_pos["deb_x"]
    if "fin_x" in dic_pos:
        coord_x += dic_pos["fin_x"]

    coord_y = liste_coord(deb_y, fin_y, nbr_y, marge)

    if "deb_y" in dic_pos:
        coord_y += dic_pos["deb_y"]
    if "fin_y" in dic_pos:
        coord_y += dic_pos["fin_y"]

    rencontre = créa_dico(coord_x)
    initialisation_dico(rencontre, deb_x, deb_y, fin_x, fin_y, coord_y)

    dico_x = créa_dico(coord_x)
    initialisation_dico(dico_x, deb_x, deb_y, fin_x, fin_y, coord_y)

    dico_y = créa_dico(coord_y)
    initialisation_dico(dico_y, deb_y, deb_x, fin_y, fin_x, coord_x)

    possibilités_début_y = {}
    ou_il_faut_passer = {}
    for y in coord_y:
        possibilités_début_y[y] = list(coord_x)
        ou_il_faut_passer[y] = []

    # print(coord_y)

    # faire toutes les colonnes aléatoirement
    place_prise_par_colonnes = [fin_y, deb_y]
    place_prise_par_lignes = [fin_x, deb_x]

    for i in range(len(coord_x) - 2):
        if "deb_x" in dic_pos or "fin_x" in dic_pos:
            if "deb_x" in dic_pos:
                if coord_x[i + 2] in dic_pos["deb_x"]:
                    debut = deb_y
                else:
                    debut = choice(coord_y)
            if "fin_x" in dic_pos:
                if coord_x[i + 2] in dic_pos["fin_x"]:
                    debut = fin_y
                else:
                    debut = choice(coord_y)
        else:
            debut = choice(coord_y)

        fin = choice(coord_y)

        while debut == fin:
            fin = choice(coord_y)

        place_prise_par_colonnes[0] = min(place_prise_par_colonnes[0], debut, fin)
        place_prise_par_colonnes[1] = max(place_prise_par_colonnes[1], debut, fin)

        dico_x[coord_x[i + 2]].append(debut)
        dico_x[coord_x[i + 2]].append(fin)

        if debut == 0 or debut == height:
            rencontre[coord_x[i + 2]].append(debut)
        else:
            possibilités_début_y[debut].remove(coord_x[i + 2])
            ou_il_faut_passer[debut].append(coord_x[i + 2])

        if fin == 0 or fin == height:
            rencontre[coord_x[i + 2]].append(fin)
        else:
            possibilités_début_y[fin].remove(coord_x[i + 2])
            ou_il_faut_passer[fin].append(coord_x[i + 2])

        for y in possibilités_début_y:
            if (fin < y and debut < y) or (fin > y and debut > y):
                possibilités_début_y[y].remove(coord_x[i + 2])

    pas_de_barre(
        coord_x,
        rencontre,
        dico_x,
        place_prise_par_colonnes,
        fin_y,
        marge,
    )

    for y in coord_y:
        possibilités_début_y[y].sort()

        debut = 0
        fin = 0

        if "deb_y" in dic_pos:
            if y in dic_pos["deb_y"]:
                debut = deb_x
        if "fin_y" in dic_pos:
            if y in dic_pos["fin_y"]:
                debut = fin_x

        if ou_il_faut_passer[y] != []:

            i_min = 1
            while possibilités_début_y[y][i_min] < min(ou_il_faut_passer[y]):
                i_min += 1

            i_max = 0
            while possibilités_début_y[y][i_max] < max(ou_il_faut_passer[y]):
                i_max += 1

            if debut >= possibilités_début_y[y][i_min]:
                fin = debut
                debut = 0

            if debut == 0:
                debut = possibilités_début_y[y][randrange(i_min)]
            if fin == 0:
                fin = possibilités_début_y[y][
                    randrange(i_max, len(possibilités_début_y[y]))
                ]

        else:
            if debut == 0:
                debut = choice(possibilités_début_y[y])
            if fin == 0:
                fin = choice(possibilités_début_y[y])

        # print(y, debut, fin)

        if y != 0 and y != height:
            dico_y[y].append(debut)
            dico_y[y].append(fin)

        place_prise_par_lignes[0] = min(place_prise_par_lignes[0], debut, fin)
        place_prise_par_lignes[1] = max(place_prise_par_lignes[1], debut, fin)

        for deb_x in coord_x:
            if (
                dico_x[deb_x][0] <= deb_y <= dico_x[deb_x][1]
                or dico_x[deb_x][0] >= deb_y >= dico_x[deb_x][1]
            ) and (
                debut == deb_x
                or fin == deb_x
                or (fin < deb_x < debut)
                or (debut < deb_x < fin)
            ):
                rencontre[deb_x].append(deb_y)
                # rencontre[deb_x].sort()

    pas_de_barre(
        coord_y,
        rencontre,
        dico_y,
        place_prise_par_lignes,
        fin_x,
        marge,
    )

    return {
        "rencontre": rencontre,
        "dico_x": dico_x,
        "dico_y": dico_y,
        "possibilités_début_y": possibilités_début_y,
        "ou_il_faut_passer": ou_il_faut_passer,
    }
