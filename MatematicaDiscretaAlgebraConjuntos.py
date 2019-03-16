a = [1, 2, 3, 4]
b = [5, 4, 6, 7, 1, 2]
c = []


def inserir(x, y):
    if x not in y:
        y.append(x)


def remover(x, y):
    if x in y:
        y.remove(x)

def pertinencia(x, y):
    if x in y:
        print("Pertence")
    else:
        print("Não Pertence")

def continencia(x,y):
    for i in x:
        print(i)
        if i not in y:
            print("Não contém")
        else:
            print("Contém")

def uniao():
    for i in a:
        inserir(i, c)
    for j in b:
        inserir(j, c)
    print(c)

def complemento(x,y):
    for i in x:
        if i not in y:
            c.append(i)
    print(c)

# uniao()
# pertinencia(10, c)
# pertinencia(5, c)
# continencia(a,b)
complemento(a,b)
