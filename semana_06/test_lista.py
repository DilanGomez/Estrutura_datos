# Código base — Semana 06
# Fuente: 01-Momento-1-Contrato-y-secuencia/06-Semana-06-Listas-enlazadas-simples/02-guia-de-laboratorio.html

from lista_arreglo import ListaArreglo
from lista_enlazada import ListaEnlazada

# ANTES:  IMPLEMENTACIONES = [ListaArreglo]
IMPLEMENTACIONES = [ListaArreglo, ListaEnlazada]

# No cambies NADA más. Ejecuta:
#     pytest -v
# Deberías ver cada prueba corriendo dos veces, una por implementación.

import random

import pytest

from lista_arreglo import PosicionInvalidaError


# ---------- pruebas del contrato, una vez por implementación ----------

def llenar(Lista, valores):
    lista = Lista()
    for i, v in enumerate(valores):
        lista.insertar(i, v)
    return lista


@pytest.mark.parametrize("Lista", IMPLEMENTACIONES)
def test_vacia(Lista):
    lista = Lista()
    assert lista.tamaño() == 0 and len(lista) == 0
    assert lista.buscar("x") == -1


@pytest.mark.parametrize("Lista", IMPLEMENTACIONES)
def test_un_elemento(Lista):
    lista = llenar(Lista, ["a"])
    assert lista.obtener(0) == "a"
    assert lista.buscar("a") == 0
    assert lista.eliminar(0) == "a"
    assert lista.tamaño() == 0


@pytest.mark.parametrize("Lista", IMPLEMENTACIONES)
def test_insertar_inicio_medio_final(Lista):
    lista = llenar(Lista, ["b", "d"])
    lista.insertar(0, "a")          # inicio
    lista.insertar(2, "c")          # medio
    lista.insertar(4, "e")          # final
    assert list(lista) == ["a", "b", "c", "d", "e"]


@pytest.mark.parametrize("Lista", IMPLEMENTACIONES)
def test_eliminar_inicio_medio_final(Lista):
    lista = llenar(Lista, ["a", "b", "c", "d", "e"])
    assert lista.eliminar(0) == "a"
    assert lista.eliminar(1) == "c"
    assert lista.eliminar(2) == "e"
    assert list(lista) == ["b", "d"]


@pytest.mark.parametrize("Lista", IMPLEMENTACIONES)
def test_buscar_primera_aparicion(Lista):
    lista = llenar(Lista, ["a", "b", "a"])
    assert lista.buscar("a") == 0
    assert lista.buscar("z") == -1


@pytest.mark.parametrize("Lista", IMPLEMENTACIONES)
def test_posiciones_invalidas(Lista):
    lista = llenar(Lista, ["a"])
    for operacion in (lambda: lista.obtener(1), lambda: lista.obtener(-1),
                      lambda: lista.insertar(2, "x"), lambda: lista.insertar(-1, "x"),
                      lambda: lista.eliminar(1), lambda: Lista().eliminar(0)):
        with pytest.raises(PosicionInvalidaError):
            operacion()
    assert list(lista) == ["a"]     # un error no modifica la lista


@pytest.mark.parametrize("Lista", IMPLEMENTACIONES)
def test_crece_mas_alla_de_la_capacidad(Lista):
    lista = Lista()
    for i in range(100):
        lista.insertar(0, i)
    assert list(lista) == list(range(99, -1, -1))


@pytest.mark.parametrize("Lista", IMPLEMENTACIONES)
def test_estres_contra_modelo(Lista):
    """Operaciones aleatorias comparadas con una list de Python como oráculo."""
    rng = random.Random(7)
    lista, modelo = Lista(), []
    for _ in range(2000):
        if modelo and rng.random() < 0.4:
            pos = rng.randrange(len(modelo))
            assert lista.eliminar(pos) == modelo.pop(pos)
        else:
            pos = rng.randint(0, len(modelo))
            valor = rng.randint(0, 50)
            lista.insertar(pos, valor)
            modelo.insert(pos, valor)
        assert lista.tamaño() == len(modelo)
    assert list(lista) == modelo