from countingSort import countingSort

def test_lista_vazia():
    lista = []
    resultado = countingSort(lista)
    assert resultado == []

def test_lista_unico_elemento():
    lista = [1]
    resultado = countingSort(lista)
    assert resultado == [1]

def test_lista_ordenada():
    lista = [1,2,3,4,5]
    resultado = countingSort(lista)
    assert resultado == [1,2,3,4,5]
def test_lista_inversamente_ordenada():
    lista = [5,4,3,2,1]
    resultado = countingSort(lista)
    assert resultado == [1,2,3,4,5]

def test_lista_desordenada():
    lista = [3,1,4,2,5]
    resultado = countingSort(lista)
    assert resultado == [1,2,3,4,5]

def test_lista_repetidos():
    lista = [3,1,2,1,3]
    resultado = countingSort(lista)
    assert resultado == [1,1,2,3,3]

def test_lista_com_zero():
    lista = [0,1,2,0,2,1]
    resultado = countingSort(lista)
    assert resultado == [0,0,1,1,2,2]
