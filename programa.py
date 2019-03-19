import itertools

a = [1, 2, 3, 4]
b = [5, 4, 6, 7, 1, 2]


def inserir(x, y):
    if x not in y:
        y.append(x)
    return y


def pertinencia(x, y):
    if x in y:
        print("Pertence")
    else:
        print("Não Pertence")


def continencia(x, y):
    for i in x:
        if i not in y:
            print("Não contém")
        else:
            print("Contém")


def uniao(x,y):
    c = []
    for i in x:
        inserir(i, c)
    for j in y:
        inserir(j, c)
    print(c)


def interserccao(x, y):
    z = []
    for i in x:
        if i in y:
            z.append(i)
    print(z)


def diferenca(x, y):
    z = []
    for i in x:
        if i not in y:
            z.append(i)
    print(z)


def complemento(x, y):
    w = []
    z = []
    for i in x:
        if i not in y:
            w.append(i)
    print("Complemento A-B: ", w)
    for j in y:
        if j not in x:
            z.append(j)
    print("Complemento B-A: ", z)


def conjuntoDasPartes(x, y):
    w = []
    z = []
    for i in range(len(x) + 1):
        w.append(list(itertools.combinations(x, i)))
    print(w)
    for j in range(len(y) + 1):
        z.append(list(itertools.combinations(y, j)))
    print(z)


def produtoCartesiano(x, y):
    for i in x:
        for j in y:
            print('(x:{0} y:{1})'.format(i, j))


def uniaoDisjunta(x, y):
    z = []
    for i in x:
        z.append([i, 'A'])
    for j in y:
        z.append([j, 'B'])
    print(z)


# pertinencia(10, c)
# pertinencia(5, c)
# continencia(a,b)
# uniao(a, b)
# interserccao(a,b)
# diferenca(a,b)
# complemento(a,b)
# conjuntoDasPartes(a, b)
# produtoCartesiano(a,b)
# uniaoDisjunta(a,b)
