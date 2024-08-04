from linearSearch import linearSearch

def test_key_inicio():
    lista1 = [2, 3, 4, 10, 40]
    key = 2
    resultado = linearSearch(lista1, key)
    assert resultado == 'O número 2 encontra-se na posição 0 da lista'

def test_key_fim():
    lista1 = [2, 3, 4, 10, 40]
    key = 40
    resultado = linearSearch(lista1, key)
    assert resultado == 'O número 40 encontra-se na posição 4 da lista'

def test_key_meio():
    lista1 = [2, 3, 4, 10, 40]
    key = 4
    resultado = linearSearch(lista1, key)
    assert resultado == 'O número 4 encontra-se na posição 2 da lista'

def test_key_inexistente():
    lista1 = [2, 3, 4, 10, 40]
    key = 1
    resultado = linearSearch(lista1, key)
    assert resultado == -1

def test_key_vazia():
    lista1 = []
    key = 2
    resultado = linearSearch(lista1, key)
    assert resultado == -1