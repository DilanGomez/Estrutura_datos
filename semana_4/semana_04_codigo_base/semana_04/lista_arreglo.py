# Código base — Semana 04
# Adaptado para el ejercicio de búsqueda lineal y binaria

class PosicionInvalidaError(IndexError):
    """La posición solicitada está fuera del rango válido."""


class ListaArreglo:
    """Lista implementada sobre un arreglo con redimensionamiento.

    Complejidad:
        obtener          -> O(1)
        insertar(final)  -> O(1) amortizado
        insertar(inicio) -> O(n)
        insertar_ordenado -> O(n)
        buscar_lineal    -> O(n)
        buscar_binaria   -> O(log n)
    """

    CAPACIDAD_INICIAL = 4

    def __init__(self):
        self._capacidad = self.CAPACIDAD_INICIAL
        self._datos = [None] * self._capacidad
        self._tamaño = 0

    # ---------- operaciones públicas ----------

    def tamaño(self):
        """Devuelve la cantidad de elementos almacenados."""
        return self._tamaño

    def insertar(self, posicion, elemento):
        """Inserta un elemento en una posición y desplaza los siguientes."""
        self._validar(posicion, incluir_final=True)

        if self._tamaño == self._capacidad:
            self._redimensionar(self._capacidad * 2)

        # Se desplaza desde el final para no sobrescribir elementos.
        i = self._tamaño
        while i > posicion:
            self._datos[i] = self._datos[i - 1]
            i = i - 1

        self._datos[posicion] = elemento
        self._tamaño = self._tamaño + 1

    def insertar_ordenado(self, elemento):
        """Inserta el elemento conservando el orden ascendente."""
        izquierda = 0
        derecha = self._tamaño

        # Primero encuentra la posición con búsqueda binaria.
        while izquierda < derecha:
            medio = (izquierda + derecha) // 2

            if self._datos[medio] < elemento:
                izquierda = medio + 1
            else:
                derecha = medio

        self.insertar(izquierda, elemento)

    def obtener(self, posicion):
        """Devuelve el elemento almacenado en la posición indicada."""
        self._validar(posicion, incluir_final=False)
        return self._datos[posicion]

    def buscar_lineal(self, elemento):
        """Busca recorriendo los elementos desde el principio."""
        for i in range(self._tamaño):
            if self._datos[i] == elemento:
                return i
        return -1

    def buscar_binaria(self, elemento):
        """Busca un elemento mediante búsqueda binaria.

        La lista debe estar ordenada de menor a mayor.
        """
        izquierda = 0
        derecha = self._tamaño - 1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2

            if self._datos[medio] == elemento:
                return medio

            if self._datos[medio] < elemento:
                izquierda = medio + 1
            else:
                derecha = medio - 1

        return -1

    # ---------- auxiliares ----------

    def _validar(self, posicion, incluir_final):
        limite = self._tamaño if incluir_final else self._tamaño - 1

        if not 0 <= posicion <= limite:
            raise PosicionInvalidaError(
                f"posicion {posicion} fuera de rango [0, {limite}]"
            )

    def _redimensionar(self, nueva_capacidad):
        """Crea un arreglo mayor y copia los elementos."""
        nuevos_datos = [None] * nueva_capacidad

        i = 0
        while i < self._tamaño:
            nuevos_datos[i] = self._datos[i]
            i = i + 1

        self._datos = nuevos_datos
        self._capacidad = nueva_capacidad

    # ---------- protocolo de Python ----------

    def __len__(self):
        return self._tamaño

    def __getitem__(self, i):
        return self.obtener(i)

    def __iter__(self):
        for i in range(self._tamaño):
            yield self._datos[i]

    def __repr__(self):
        return f"ListaArreglo({[x for x in self]!r})"