from random import randrange


def liste_coord(deb, fin, nbr_coord, marge):
    marge_init = marge
    liste = [deb, fin]
    for i in range(nbr_coord):
        trop_près = 1
        garde_fou = 0
        while trop_près != 0:
            if garde_fou >= 10:
                marge -= 10
            elif garde_fou >= 20:
                marge -= 20
            elif garde_fou >= 30:
                marge -= 30
            coord_nouv = randrange(int(deb + marge), int(fin - marge))
            trop_près = 0
            for coord_deja_la in liste:
                if abs(coord_nouv - coord_deja_la) < marge:
                    trop_près += 1
                    garde_fou = 0
            garde_fou += 1
            marge = marge_init

        liste.append(coord_nouv)
    return liste


def créa_dico(liste_clés):
    dico = {}
    for clé in liste_clés:
        dico[clé] = []
    return dico


def initialisation_dico(dico, deb_c1, deb_c2, fin_c1, fin_c2, coord_c2):
    dico[deb_c1].append(deb_c2)
    for i in range(2):
        dico[deb_c1].append(fin_c2)
    dico[fin_c1].append(deb_c2)
    for i in range(2):
        dico[fin_c1].append(fin_c2)


def pas_de_barre(coord_c1, rencontre, dico_c2, place_prise_par_trait, fin_c2, marge):

    deb_c1 = min(coord_c1)
    fin_c1 = max(coord_c1)

    # print(place_prise_par_trait)

    if place_prise_par_trait[0] != 0:
        coord_encore_nouv = randrange(int(deb_c1 + marge), int(fin_c1 - marge))
        coord_c1.append(coord_encore_nouv)
        rencontre[coord_encore_nouv] = [0, min(place_prise_par_trait)]
        dico_c2[coord_encore_nouv] = [0, min(place_prise_par_trait)]

    if place_prise_par_trait[1] != fin_c2:
        coord_encore_nouv = randrange(int(deb_c1 + marge), int(fin_c1 - marge))
        coord_c1.append(coord_encore_nouv)
        rencontre[coord_encore_nouv] = [max(place_prise_par_trait), fin_c2]
        dico_c2[coord_encore_nouv] = [max(place_prise_par_trait), fin_c2]
