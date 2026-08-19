# Código base — Semana 02
# Fuente: 01-Momento-1-Contrato-y-secuencia/02-Semana-02-ADT-y-Spec-Driven-Development/02-guia-de-laboratorio.html

from bolsa_lista import ElementoNoEncontradoError
class BolsaDict:
    """Bolsa implementada como diccionario de conteos.

    Complejidad:
        agregar  -> O(1)
        sacar    -> O(1)
        cuantos  -> O(1)
        tamaño   -> O(1)
        contiene -> O(1)
    """

    def __init__(self):
        self._conteos = {}
        self._total = 0

    def agregar(self, elemento):
        if elemento in self._conteos:
            self._conteos[elemento] += 1
        else:
            self._conteos[elemento] = 1

        self._total += 1
        pass

    def sacar(self, elemento):
           if elemento not in self._conteos:
            raise ElementoNoEncontradoError()

           self._conteos[elemento] -= 1
           self._total -=1

           if self._conteos[elemento] == 0:
               del self._conteos[elemento]
          

    pass

    def cuantos(self, elemento):
        return self._conteos.get(elemento, 0)
    pass

    def tamaño(self):
        return self._total
    pass

    def contiene(self, elemento):
     return elemento in self._conteos
    pass