from bubbleSort import bubbleSort

def test_lista_vazia():
    lista = []
    resultado = bubbleSort(lista)
    assert resultado == []

def test_lista_unico_elemento():
    lista = [1]
    resultado = bubbleSort(lista)
    assert resultado == [1]

def test_lista_ordenada():
    lista = [1,2,3,4,5]
    resultado = bubbleSort(lista)
    assert resultado == [1,2,3,4,5]

def test_lista_inversa():
    lista = [6,5,4,3,2,1]
    resultado = bubbleSort(lista)
    assert resultado == [1,2,3,4,5,6]

def test_lista_desordenada():
    lista = [5,2,3,1,4]
    resultado = bubbleSort(lista)
    assert resultado == [1,2,3,4,5]

def test_lista_repeticoes():
    lista = [1,3,2,3,1]
    resultado = bubbleSort(lista)
    assert resultado == [1,1,2,3,3]