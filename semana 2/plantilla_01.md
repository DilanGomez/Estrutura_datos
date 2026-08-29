# Especificación — ADT Bolsa

## 1. Propósito

Una bolsa es una estructura de datos que almacena elementos permitiendo repeticiones, sin mantener un orden definido. Permite agregar elementos, eliminarlos, consultar cuántas veces aparece un elemento y conocer el tamaño total de la colección.

## 2. Fuera de alcance

* No mantiene el orden de inserción.
* No permite acceder a elementos por posición o índice.
* No realiza ordenamiento de elementos.
* No diferencia elementos por prioridad.
* No realiza búsquedas parciales o por patrones.

## 3. Operaciones

### agregar(elemento)

**Precondiciones**

* Ninguna.

**Postcondiciones**

* La cantidad de apariciones de `elemento` aumenta en 1.
* El tamaño total de la bolsa aumenta en 1.

**Errores**

* Ninguno.

---

### sacar(elemento)

**Precondiciones**

* El elemento debe existir al menos una vez en la bolsa.

**Postcondiciones**

* La cantidad de apariciones de `elemento` disminuye en 1.
* El tamaño total de la bolsa disminuye en 1.
* Si la cantidad llega a cero, el elemento deja de existir en la bolsa.

**Errores**

* Lanza `ElementoNoEncontradoError` si el elemento no existe.

---

### cuantos(elemento)

**Precondiciones**

* Ninguna.

**Postcondiciones**

* Devuelve el número de veces que aparece `elemento` en la bolsa.

**Errores**

* Ninguno.

**Caso especial**

* Si el elemento no existe, devuelve 0.

---

### tamaño()

**Precondiciones**

* Ninguna.

**Postcondiciones**

* Devuelve el número total de elementos almacenados, incluyendo repeticiones.

**Errores**

* Ninguno.

---

### contiene(elemento)

**Precondiciones**

* Ninguna.

**Postcondiciones**

* Devuelve `True` si el elemento existe al menos una vez.
* Devuelve `False` en caso contrario.

**Errores**

* Ninguno.

## 4. Invariantes

* **INV-01:** El tamaño de la bolsa siempre es mayor o igual a cero.
* **INV-02:** El tamaño total es igual a la suma de las cantidades de todos los elementos almacenados.
* **INV-03:** Ningún elemento puede tener una cantidad negativa.
* **INV-04:** Un elemento con cantidad cero no debe almacenarse en la bolsa.

## 5. Criterios de aceptación

ID	Criterio	                                                             Prueba que lo verifica
CA-01	Una bolsa recién creada tiene tamaño 0	                             test_bolsa_vacia
CA-02	Agregar el mismo elemento dos veces hace que cuantos() devuelva 2	 test_duplicados
CA-03	Sacar un elemento inexistente lanza ElementoNoEncontradoError	     test_sacar_inexistente
CA-04	Sacar un elemento existente reduce la cantidad y el tamaño en 1                                                                       test_sacar_reduce_cantidad
CA-05	Consultar un elemento inexistente devuelve 0	          test_cantidad_producto_inexistente
CA-06	El tamaño siempre coincide con la suma de las cantidades almacenadas          |                                                     test_invariante_tamaño

## 6. Casos extremos considerados

* Bolsa vacía.
* Un único elemento.
* Elemento repetido múltiples veces.
* Eliminación del último ejemplar de un elemento.
* Consulta de un elemento inexistente.
* Intento de eliminar un elemento inexistente.
* Verificación de invariantes después de varias operaciones consecutivas.
