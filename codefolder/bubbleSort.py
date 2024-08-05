def bubbleSort(lista):
    for n in range(len(lista),0,-1):
        shift = False
        for i in range(0, n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                shift = True
        if not shift:
            break
    return lista