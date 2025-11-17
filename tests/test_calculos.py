import pytest
from mi_paquete.calculos import sumar, dividir

def test_sumar_entero():
    assert sumar(2, 3) == 5

def test_sumar_negativos():
    assert sumar(-1, -2) == -3

def test_sumar_floats():
    assert abs(sumar(1.2, 3.4) - 4.6) < 1e-9

def test_dividir_valor():
    assert dividir(6, 3) == 2

def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)
