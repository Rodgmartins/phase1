def linearSearch(lista, key):
    for i in range(len(lista)):
        if lista[i] == key:
            return f"O número {lista[i]} encontra-se na posição {i} da lista"
        else:
            return -1