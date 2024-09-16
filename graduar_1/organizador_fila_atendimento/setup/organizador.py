def gerador_numerico(stop):
    contador = 0
    fila = []
    num_stop = stop

    while contador <= num_stop:
        fila.append(contador)
        contador += 1

    return fila

