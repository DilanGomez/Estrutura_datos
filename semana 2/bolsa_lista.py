# Código base — Semana 02
# Fuente: 01-Momento-1-Contrato-y-secuencia/02-Semana-02-ADT-y-Spec-Driven-Development/02-guia-de-laboratorio.html

class ElementoNoEncontradoError(Exception):
    """El elemento solicitado no está en la bolsa."""


class BolsaLista:
    """Bolsa implementada sobre una lista: un elemento por cada aparición.

    Complejidad:
        agregar  -> O(1)
        sacar    -> O(n)
        cuantos  -> O(n)
        tamaño   -> O(1)
        contiene -> O(n)
    """

    def __init__(self):
        self._elementos = []

    def agregar(self, elemento):
        self._elementos.append(elemento)
        pass

    def sacar(self, elemento):
        if elemento not in self._elementos:
            raise ElementoNoEncontradoError()
        
        self._elementos.remove(elemento)
        pass

    def cuantos(self, elemento):
          cantidad = 0

          for e in self._elementos:
            if e == elemento:
                cantidad += 1

                return cantidad

    pass

    def tamaño(self):
        return len(self._elementos)
        pass

    def contiene(self, elemento):
        return elemento in self._elementos

    pass

    def __len__(self):
        return self.tamaño()

    def __repr__(self):
        return f"BolsaLista({self._elementos!r})"

