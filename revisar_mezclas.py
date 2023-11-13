import random
def ordenar_cartas(l1,l2):
    p = 0
    n = 0
    numeros_revisados = 0
    random.shuffle(posicion_x)
    random.shuffle(posicion_y)
    while True:
        for x,y in zip(posicion_x[p:],posicion_y[p:]):
            n += 1
            numeros_revisados += 1
            break
        for x2,y2 in zip(posicion_x[n:],posicion_y[n:]):
            if x == x2 and y == y2:
                p = -1
                n = 0
                numeros_revisados = 0
                random.shuffle(posicion_x)
                random.shuffle(posicion_y)
                numeros_revisados += 1
                break
        if numeros_revisados == 10:break
        p += 1
    return posicion_x, posicion_y
posicion_x = [53,53,294,294,531,531,769,769,1015,1015]
posicion_y = [20,20,20,20,20,361,361,361,361,361]