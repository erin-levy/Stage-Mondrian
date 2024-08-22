def déplacement_quadrillage(dicos, d_c1, d_c2):
    dic_nouv = []
    for i in range(len(dicos)):
        for coord in dicos[i]:
            dicos[i][coord][0] += d_c2
            dicos[i][coord][1] += d_c2
        dic_nouv.append({})
        for x in dicos[i]:
            dic_nouv[i][x + d_c1] = dicos[i][x]
    return dic_nouv


def zoom_quadrillage(c1, c2, dicos_c1, grandissement):

    dic_nouv_x = []
    for i in range(len(dicos_c1)):
        dic_nouv_x.append({})
        for coord1 in dicos_c1[i]:
            dicos_c1[i][coord1][0] += (dicos_c1[i][coord1][0] - c2) * grandissement
            dicos_c1[i][coord1][1] += (dicos_c1[i][coord1][1] - c2) * grandissement
            if len(dicos_c1[i][coord1]) == 3:
                dicos_c1[i][coord1][2] += (dicos_c1[i][coord1][2] - c2) * grandissement
            dic_nouv_x[i][coord1 + (coord1 - c1) * grandissement] = dicos_c1[i][coord1]

    return dic_nouv_x


def fusion_dico(dico1, dico2):
    for c in dico2:
        if c in dico1:
            dico1[c] += dico2[c]
        else:
            dico1[c] = dico2[c]
    return dico1


def dico_bords(dic, i, j, dico_x, dico_y):
    coord_x = list(dico_x.keys())
    x = coord_x[0]
    width = coord_x[1]

    coord_y = list(dico_y.keys())
    y = coord_y[0]
    height = coord_y[1]

    if (i, j + 1) not in dic:
        dic[(i, j + 1)] = {}

    if (i, j - 1) not in dic:
        dic[(i, j - 1)] = {}

    if (i + 1, j) not in dic:
        dic[(i + 1, j)] = {}

    if (i - 1, j) not in dic:
        dic[(i - 1, j)] = {}

    dic[(i, j + 1)]["deb_x"] = []
    dic[(i, j - 1)]["fin_x"] = []
    dic[(i + 1, j)]["deb_y"] = []
    dic[(i - 1, j)]["fin_y"] = []

    for x1 in dico_x:
        if len(dico_x[x1]) == 2:
            if dico_x[x1][0] == height or dico_x[x1][1] == height:
                dic[(i, j + 1)]["deb_x"].append(x1)
            if dico_x[x1][0] == y or dico_x[x1][1] == y:
                dic[(i, j - 1)]["fin_x"].append(x1)

    for y1 in dico_y:
        if len(dico_y[y1]) == 2:
            if dico_y[y1][0] == width or dico_y[y1][1] == width:
                dic[(i + 1, j)]["deb_y"].append(y1)
            if dico_y[y1][0] == x or dico_y[y1][1] == x:
                dic[(i - 1, j)]["fin_y"].append(y1)

    return dic


def coord_nouv(i, j, debut_x, debut_y, width, height):
    deb_x = i * width + debut_x
    deb_y = j * height + debut_y

    return (deb_x, deb_y)
