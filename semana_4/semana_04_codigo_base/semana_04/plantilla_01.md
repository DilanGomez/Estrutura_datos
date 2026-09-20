# Especificación — ADT ListaArreglo

## 1. Propósito

Colección ordenada de elementos almacenados sobre un arreglo, accesibles por
posición. Permite insertar elementos en cualquier posición, insertar
manteniendo el orden y realizar búsquedas lineales o binarias.

## 2. Operaciones

### insertar(posicion, elemento)

- Precondiciones: `0 <= posicion <= tamaño`
- Postcondiciones: el elemento queda en `posicion`; el tamaño aumenta en 1;
  los elementos que estaban desde esa posición se desplazan una posición a
  la derecha.
- Errores: `PosicionInvalidaError`
- Complejidad: `O(n)` en el peor caso.

### insertar_ordenado(elemento)

- Precondiciones: los elementos existentes están ordenados de menor a mayor.
- Postcondiciones: el nuevo elemento queda en la posición que corresponde y
  la lista continúa ordenada; el tamaño aumenta en 1.
- Complejidad: `O(n)` en el peor caso. La posición se encuentra con búsqueda
  binaria `O(log n)`, pero insertar requiere desplazar elementos `O(n)`.

### obtener(posicion) -> elemento

- Precondiciones: `0 <= posicion < tamaño`
- Postcondiciones: devuelve el elemento almacenado en esa posición sin
  modificar la lista.
- Errores: `PosicionInvalidaError`
- Complejidad: `O(1)`.

### buscar_lineal(elemento) -> posicion o -1

- Precondiciones: ninguna.
- Postcondiciones: devuelve la primera posición donde aparece el elemento o
  `-1` si no está.
- Complejidad: `O(n)` en el peor caso.

### buscar_binaria(elemento) -> posicion o -1

- Precondiciones: la lista debe estar ordenada de menor a mayor.
- Postcondiciones: devuelve una posición donde aparece el elemento o `-1` si
  no está; la lista no se modifica.
- Complejidad: `O(log n)` en el peor caso.

### tamaño() -> entero

- Postcondiciones: devuelve la cantidad de elementos almacenados.
- Complejidad: `O(1)`.

## 3. Invariantes

- INV-01: `0 <= tamaño <= capacidad`.
- INV-02: los elementos ocupan exactamente las posiciones
  `0` hasta `tamaño - 1`.
- INV-03: `obtener(i)` devuelve el elemento almacenado en la posición `i`.
- INV-04: después de `insertar_ordenado`, los elementos quedan ordenados de
  menor a mayor.
- INV-05: `buscar_binaria` solo se utiliza sobre una lista ordenada.

## 4. Conteo de operaciones

| Operación | Conteo aproximado en el peor caso | Complejidad |
|---|---:|---:|
| `obtener` | 1 acceso | `O(1)` |
| `insertar` al final | 1 escritura | `O(1)` amortizado |
| `insertar` al inicio | hasta `n` desplazamientos | `O(n)` |
| `insertar_ordenado` | hasta `log₂(n)` comparaciones + hasta `n` desplazamientos | `O(n)` |
| `buscar_lineal` | hasta `n` comparaciones | `O(n)` |
| `buscar_binaria` | hasta `log₂(n)` comparaciones | `O(log n)` |

## 5. Criterios de aceptación

| ID | Criterio | Prueba |
|---|---|---|
| CA-01 | Una lista nueva tiene tamaño 0 | `test_lista_vacia` |
| CA-02 | Insertar en posición 0 en lista vacía deja el elemento accesible | `test_insertar_en_vacia` |
| CA-03 | Insertar al inicio desplaza los elementos sin perderlos | `test_insertar_inicio` |
| CA-04 | Insertar al final conserva los elementos anteriores | `test_insertar_final` |
| CA-05 | `obtener` devuelve el elemento correcto | `test_obtener` |
| CA-06 | `insertar_ordenado` mantiene el orden | `test_insertar_ordenado` |
| CA-07 | `buscar_lineal` encuentra un elemento y devuelve -1 si no existe | `test_buscar_lineal` |
| CA-08 | `buscar_binaria` encuentra un elemento y devuelve -1 si no existe | `test_buscar_binaria` |
| CA-09 | Una lista vacía funciona correctamente con las búsquedas | `test_busquedas_lista_vacia` |
| CA-10 | Una lista de un elemento funciona correctamente | `test_un_elemento` |
| CA-11 | Una posición inválida produce `PosicionInvalidaError` | `test_posicion_invalida` |
| CA-12 | Redimensionar no pierde los elementos | `test_redimensionamiento` |

