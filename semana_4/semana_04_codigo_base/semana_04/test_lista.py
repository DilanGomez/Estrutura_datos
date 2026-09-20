# Código base — Semana 04
# Pruebas para ListaArreglo

import pytest
from lista_arreglo_simple import ListaArreglo, PosicionInvalidaError


def test_lista_vacia():
    """Una lista nueva tiene tamaño 0."""
    lista = ListaArreglo()

    assert lista.tamaño() == 0


def test_insertar_en_vacia():
    """Insertar en posición 0 en una lista vacía."""
    lista = ListaArreglo()

    lista.insertar(0, "a")

    assert lista.tamaño() == 1
    assert lista.obtener(0) == "a"


def test_un_elemento():
    """Una lista con un elemento permite obtenerlo y buscarlo."""
    lista = ListaArreglo()

    lista.insertar(0, "a")

    assert lista.obtener(0) == "a"
    assert lista.buscar_lineal("a") == 0
    assert lista.buscar_binaria("a") == 0


def test_insertar_inicio():
    """Insertar al inicio desplaza los elementos existentes."""
    lista = ListaArreglo()

    lista.insertar(0, "b")
    lista.insertar(1, "c")
    lista.insertar(0, "a")

    assert [lista.obtener(i) for i in range(3)] == ["a", "b", "c"]


def test_insertar_final():
    """Insertar al final conserva los elementos anteriores."""
    lista = ListaArreglo()

    lista.insertar(0, "a")
    lista.insertar(1, "b")
    lista.insertar(2, "c")

    assert [lista.obtener(i) for i in range(3)] == ["a", "b", "c"]
    assert lista.tamaño() == 3


def test_insertar_ordenado():
    """Insertar ordenadamente mantiene la lista de menor a mayor."""
    lista = ListaArreglo()

    lista.insertar_ordenado(5)
    lista.insertar_ordenado(2)
    lista.insertar_ordenado(8)
    lista.insertar_ordenado(1)

    assert [lista.obtener(i) for i in range(4)] == [1, 2, 5, 8]


def test_buscar_lineal():
    """La búsqueda lineal encuentra elementos y devuelve -1 si no existen."""
    lista = ListaArreglo()

    lista.insertar(0, "a")
    lista.insertar(1, "b")
    lista.insertar(2, "c")

    assert lista.buscar_lineal("a") == 0
    assert lista.buscar_lineal("c") == 2
    assert lista.buscar_lineal("fantasma") == -1


def test_buscar_binaria():
    """La búsqueda binaria funciona sobre una lista ordenada."""
    lista = ListaArreglo()

    lista.insertar_ordenado(10)
    lista.insertar_ordenado(20)
    lista.insertar_ordenado(30)
    lista.insertar_ordenado(40)
    lista.insertar_ordenado(50)

    assert lista.buscar_binaria(10) == 0
    assert lista.buscar_binaria(30) == 2
    assert lista.buscar_binaria(50) == 4
    assert lista.buscar_binaria(99) == -1


def test_busquedas_lista_vacia():
    """Las búsquedas sobre una lista vacía devuelven -1."""
    lista = ListaArreglo()

    assert lista.buscar_lineal("a") == -1
    assert lista.buscar_binaria("a") == -1


def test_posicion_invalida():
    """Una posición fuera de rango produce PosicionInvalidaError."""
    lista = ListaArreglo()

    with pytest.raises(PosicionInvalidaError):
        lista.obtener(0)

    with pytest.raises(PosicionInvalidaError):
        lista.insertar(5, "x")


def test_redimensionamiento():
    """Redimensionar no pierde los elementos almacenados."""
    lista = ListaArreglo()

    for i in range(100):
        lista.insertar(i, i)

    assert lista.tamaño() == 100

    for i in range(100):
        assert lista.obtener(i) == i