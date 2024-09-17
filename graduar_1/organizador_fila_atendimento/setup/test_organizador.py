import pytest
from organizador import OrganizadorFila


@pytest.fixture
def organizador():
    return OrganizadorFila()


def test_add_cliente(organizador):
    organizador.add_cliente("Cliente 1")
    assert len(organizador.fila) == 1
    assert organizador.fila[1] == "Cliente 1"


def test_chamar_cliente(organizador):
    organizador.add_cliente("Cliente 1")
    organizador.add_cliente("Cliente 2")
    organizador.chamar_cliente()
    assert len(organizador.fila) == 1
    assert 1 not in organizador.fila
    assert organizador.ticket_atendido[
               1] == "Cliente 1"


def test_ver_fila(capsys, organizador):
    organizador.add_cliente("Cliente 1")
    organizador.add_cliente("Cliente 2")
    organizador.ver_fila()

    captured = capsys.readouterr()
    assert "Ticket 1: Cliente 1" in captured.out
    assert "Ticket 2: Cliente 2" in captured.out


def test_deletar_cliente(organizador):
    organizador.add_cliente("Cliente 1")
    organizador.add_cliente("Cliente 2")
    organizador.deletar_cliente()
    assert len(organizador.fila) == 1
    assert 1 not in organizador.fila


def test_tempo_espera(capsys, organizador):
    organizador.add_cliente("Cliente 1")
    organizador.add_cliente("Cliente 2")
    organizador.tempo_espera()

    captured = capsys.readouterr()
    assert "10 minutos" in captured.out
