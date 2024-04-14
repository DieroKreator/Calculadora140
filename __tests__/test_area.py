import pytest

from area.area import calcular_area_de_um_cuadrado, calcular_area_de_um_retangulo, calcular_area_de_um_triangulo
from utils.utils import ler_csv


# 2 - Crie os testes de unidade para essas três funções que criou na questão 1
def test_calcular_area_de_um_cuadrado():
    num1 = 3
    resultado_esperado = 9
    resultado_obtido = calcular_area_de_um_cuadrado(num1)

    assert resultado_esperado == resultado_obtido

def test_calcular_area_de_um_retangulo():
    num1 = 3
    num2 = 4
    resultado_esperado = 12
    resultado_obtido = calcular_area_de_um_retangulo(num1, num2)

    assert resultado_esperado == resultado_obtido

def test_calcular_area_de_um_trinagulo():
    num1 = 5
    num2 = 4
    resultado_esperado = 10
    resultado_obtido = calcular_area_de_um_triangulo(num1, num2)

    assert resultado_esperado == resultado_obtido


# 3 - Altere um desses testes de unidade para que leia uma massa de teste a partir de uma lista de valores
@pytest.mark.parametrize('num1, num2, resultado_esperado',
                         [ (5, 7, 35),
                           (1, 8, 8),
                           (10, 3, 30),
                           (4, 1.5, 6)
                         ]
                         )
def test_calcular_area_de_um_retangulo_lista(num1, num2, resultado_esperado):

    resultado_obtido = calcular_area_de_um_retangulo(num1, num2)

    assert resultado_esperado == resultado_obtido


# 4 - Altere outro desses testes de unidade para que leia uma massa de teste a partir de um arquivo csv
@pytest.mark.parametrize('num1, num2, resultado_esperado',
                            ler_csv('./fixtures/massa_area_triangulo.csv')
                         )
def test_calcular_area_de_um_trinagulo_csv(num1, num2, resultado_esperado):

    resultado_obtido = calcular_area_de_um_triangulo(float(num1), float(num2))

    assert float(resultado_esperado) == resultado_obtido