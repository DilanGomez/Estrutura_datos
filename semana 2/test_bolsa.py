# Código base — Semana 02
# Fuente: 01-Momento-1-Contrato-y-secuencia/02-Semana-02-ADT-y-Spec-Driven-Development/02-guia-de-laboratorio.html

import pytest
from bolsa_lista import BolsaLista
from bolsa_dict import BolsaDict
from bolsa_lista import ElementoNoEncontradoError

# Las MISMAS pruebas corren contra las DOS implementaciones
@pytest.fixture(params=[BolsaLista, BolsaDict])
def Bolsa(request):
    return request.param


def test_bolsa_vacia(Bolsa):
    """CA-01: una bolsa recién creada tiene tamaño 0."""
    b = Bolsa()
    assert b.tamaño() == 0
    assert not b.contiene()


    def test_agregar_producto (Bolsa):
         
         """Agrega un producto."""
         b = Bolsa()
    
         b.agregar("manzana", 3)
    
    assert b.cuantos("manzana") == 3
    assert b.total() == 3



def test_duplicados(Bolsa):
    """CA-02: agregar el mismo elemento dos veces da cuantos() == 2."""
    b = Bolsa()

    b.agregar("manzana",2)

    b.agregar("manzana",4)

    assert b.cuantos("manzana") == 2
    assert b.tamaño() == 2


def test_sacar_inexistente(Bolsa):
    """CA-03: sacar un elemento inexistente lanza excepción."""
    b = Bolsa()
    with pytest.raises(ElementoNoEncontradoError):
        b.sacar("fantasma",1)



def test_sacar_reduce_cantidad(Bolsa):
    """ sacar reduce en 1 la cantidad y el tamaño."""
    b = Bolsa()

    b.agregar("a",5)

    b.agregar("a",2)

    b.sacar ("a",2)

    assert b.cuantos("a") == 1
    assert b.tamaño() == 1


def test_cantidad_producto_inexistente(Bolsa):
    """CA-06: consultar un producto inexistente devuelve 0."""
    b = Bolsa()

    assert b.cuantos("fantasma") == 0

def test_no_permite_agregar_cero(Bolsa):
    """ no se permite agregar cantidad cero."""
    b= Bolsa()

    with pytest.raises(ValueError):
        b.agregar("a", 0)


def test_no_permite_agregar_negativos(Bolsa):
    """ no se permiten cantidades negativas."""
    b = Bolsa()

    with pytest.raises(ValueError):
        b.agregar("a", -1)   

def test_no_permite_sacar_mas_de_lo_existente(Bolsa):
    """CA-09: no se puede sacar más de lo almacenado."""
    b = Bolsa()

    b.agregar("a", 2)

    with pytest.raises(ValueError):
        b.sacar("a", 5)    


def test_invariante_tamaño(Bolsa):
    """INV-02: el tamaño es la suma de las cantidades."""
    b = Bolsa()
    for e in ["a", "b", "a", "c", "a"]:
        b.agregar(e)
    assert b.tamaño() == b.cuantos("a") + b.cuantos("b") + b.cuantos("c")
