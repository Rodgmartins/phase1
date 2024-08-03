from binarySearch import pesquisaBinario

def test_item_presente_no_meio():
    nums = [1, 2, 3, 4, 5, 6, 7]
    item = 4
    resultado = pesquisaBinario(nums, 0, len(nums)-1, item)
    assert resultado == 3

def test_item_presente_no_inicio():
    nums = [1, 2, 3, 4, 5, 6, 7]
    item = 1
    resultado = pesquisaBinario(nums, 0, len(nums)-1, item)
    assert resultado == 0

def test_item_presente_no_fim():
    nums = [1, 2, 3, 4, 5, 6, 7]
    item = 7
    resultado = pesquisaBinario(nums, 0, len(nums)-1, item)
    assert resultado == 6

def test_lista_vazia():
    nums = []
    item = 1
    resultado = pesquisaBinario(nums, 0, len(nums)-1, item)
    assert == -1

def test_lista_com_um_elemento():
    nums = [1]
    item = 1
    resultado = pesquisaBinario(nums, 0, len(nums)-1, item)
    assert resultado == 0

    item = 2
    resultado = pesquisaBinario(nums, 0, len(nums) - 1, item)
    assert resultado == -1