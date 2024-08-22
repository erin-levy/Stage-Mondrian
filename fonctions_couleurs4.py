def dichotomie(liste, val):
    deb = 0
    fin = len(liste) - 1
    milieu = (deb + fin) // 2
    while deb <= fin:
        if liste[milieu] == val:
            return milieu
        elif liste[milieu] < val:
            deb = milieu + 1
        else:
            fin = milieu - 1
        milieu = (deb + fin) // 2
    return milieu


def trouver_lignes(coord_1, coord_2, dico):
    liste_coord = list(dico.keys())
    liste_coord.sort()

    i1 = dichotomie(liste_coord, coord_1)
    i2 = i1 + 1

    c_1 = liste_coord[i1]
    c_2 = liste_coord[i2]
    while coord_2 < min(dico[c_1]) or coord_2 > max(dico[c_1]):
        i1 -= 1
        c_1 = liste_coord[i1]

    while coord_2 < min(dico[c_2]) or coord_2 > max(dico[c_2]):
        i2 += 1
        c_2 = liste_coord[i2]

    return (c_1, c_2)
