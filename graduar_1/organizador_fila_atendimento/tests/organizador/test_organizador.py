import pytest
from setup.organizador import gerador_numerico
def test_gerador_numerico():
    #given:
    stop = 10
    #When:
    response = gerador_numerico(stop)
    #Then:
    assert response == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]