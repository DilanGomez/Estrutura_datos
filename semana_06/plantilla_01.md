# Arreglo frente a lista enlazada

## Tabla de complejidad
| Operación          | ListaArreglo | ListaEnlazada | ¿Quién gana? |
|--------------------|--------------|---------------|--------------|
| obtener(i)         | O(1)         | O(n)          | Arreglo      |
| insertar al inicio | O(n)         | O(1)          | Enlazada     |
| insertar al final  | O(1) amort.  | O(1)          | Empate       |
| insertar en medio  | O(n)         | O(n)          | Enlazada (≈ 2×, misma clase O(n)) |
| eliminar al inicio | O(n)         | O(1)          | Enlazada     |
| eliminar al final  | O(1)         | O(n)          | Arreglo      |
| buscar             | O(n)         | O(n)          | Empate       |
| memoria por elem.  | 8 B por posición (una referencia); entre 8 y 16 B por elemento por la capacidad duplicada | 48 B por `Nodo` (`sys.getsizeof`, sin contar el dato) | Arreglo (≈ 3–6× menos) |

"Insertar en medio" es O(n) en las dos, pero la constante decide: con n = 10.000
el arreglo tarda 157 µs (desplaza n/2 elementos) y la enlazada 71 µs (recorre
n/2 nodos y enlaza). Misma complejidad, distinto costo por paso.

## Medición
20.000 inserciones al inicio, cada una en una lista que crece desde vacía
(`salida_medicion.txt`):

| Estructura | Tiempo |
|---|---:|
| ListaArreglo | 6,567 s |
| ListaEnlazada | 0,0069 s |

La enlazada es ≈ 950 veces más rápida en esta operación. Es O(n²) frente a
O(n) en total: 1 + 2 + … + 20.000 desplazamientos contra 20.000 enlaces.

Tiempo por operación (mediana de 9 repeticiones, n = 10.000; el resto de
tamaños está en `resultados.csv`):

| Operación | Arreglo | Enlazada |
|---|---:|---:|
| insertar al inicio | 311,5 µs | 1,4 µs |
| insertar en medio | 157,2 µs | 70,8 µs |
| obtener(n/2) | 0,1 µs | 69,8 µs |
| recorrer toda la lista | 235,9 µs | 197,5 µs |
| eliminar al inicio | 312,7 µs | 1,1 µs |
| eliminar en medio | 180,1 µs | 69,3 µs |

## ¿Cuál usarías para...?
1. **Un historial de navegación donde solo agregas y quitas del final:**
   ListaArreglo. Insertar y eliminar al final no desplazan nada (O(1)); en la
   enlazada simple quitar el último exige llegar al penúltimo (O(n)).
2. **Una cola de impresión donde agregas al final y quitas del inicio:**
   ListaEnlazada. Ambas puntas son O(1) (gracias a `_cola`). En el arreglo,
   quitar del inicio desplaza todo: 312,7 µs frente a 1,1 µs con n = 10.000.
3. **Un catálogo que se consulta mucho por índice y casi nunca cambia:**
   ListaArreglo. `obtener(i)` es O(1): 0,1 µs frente a 69,8 µs (≈ 700×) con
   n = 10.000, y el coste de insertar, que es lo que penaliza al arreglo,
   casi no se paga.
4. **Una lista de tareas donde insertas prioridades al principio:**
   ListaEnlazada. Insertar al inicio cuesta 1,4 µs frente a 311,5 µs
   (≈ 220×) con n = 10.000.

## Decisión del reproductor de la emisora

Frecuencias diarias: 40 insertar al inicio, 3 recorridos, 200 saltos a la
canción N (se toma la posición media) y 15 borrados de la canción actual.
Costo del día = Σ frecuencia × tiempo medido. El tamaño de la lista no está
dado, así que se mide con 1.000, 10.000 y 50.000 canciones. "Borrar la
canción actual" depende de dónde esté la actual, así que se calculan dos casos.

| Canción a borrar | n | Arreglo | Enlazada | Resultado |
|---|---:|---:|---:|---|
| en el medio | 1.000 | 1,537 ms | 1,409 ms | enlazada, ×1,1 |
| en el medio | 10.000 | 15,892 ms | 15,649 ms | empate (1,5 %) |
| en el medio | 50.000 | 81,357 ms | 85,707 ms | arreglo, ×1,05 |
| al inicio | 1.000 | 1,709 ms | 1,308 ms | enlazada, ×1,3 |
| al inicio | 10.000 | 17,880 ms | 14,626 ms | enlazada, ×1,2 |
| al inicio | 50.000 | 93,857 ms | 78,803 ms | enlazada, ×1,2 |

**Por qué sale casi empatado.** Cada estructura paga la operación que se le da
mal. Con n = 10.000 el arreglo gasta 12,5 ms en las 40 inserciones al inicio
(40 × 311,5 µs) y casi nada en los 200 saltos (0,02 ms). La enlazada gasta
14,0 ms en los 200 saltos (200 × 69,8 µs) y casi nada en las inserciones
(0,06 ms). Las frecuencias dadas equilibran las dos facturas: 40 × 311 µs ≈
200 × 70 µs.

**Recomendación: ListaEnlazada**, con una ventaja pequeña y con condiciones:
- Con hasta 10.000 canciones, que es un tamaño razonable para una emisora,
  la enlazada gana o empata en los dos casos de borrado: hasta 1,3× más
  rápida, es decir, entre 0 y 3,3 ms de trabajo al día.
- Solo el arreglo gana, y por 5 %, con la canción actual en el medio y
  50.000 canciones.
- La frontera está muy cerca de los datos reales. Con n = 10.000 y la canción
  actual en el medio, la enlazada deja de ganar si las inserciones al inicio
  bajan de 39 al día (hoy 40) o si los saltos suben de 203 al día (hoy 200).
  Con n = 50.000 el cruce está en 43 inserciones y 188 saltos.
- Conviene revisar la elección si la lista crece, si suben los saltos o si
  bajan las canciones de última hora.

Ambas cuestan menos de 0,1 s de trabajo al día, así que en la práctica la
velocidad casi no decide. Los datos inclinan la balanza hacia la enlazada, pero
si al equipo le importa más gastar poca memoria (el arreglo usa entre 3 y 6×
menos), el arreglo también es defendible: el margen es de un dígito porcentual.

## Conclusión
No hay ganador absoluto: hay perfiles de costo distintos, y lo que decide es
frecuencia × costo de cada operación, no la operación aislada.
Si domina el acceso por índice o el trabajo en el final, gana el arreglo; si
dominan las inserciones y borrados al inicio, gana la enlazada.
Cuando las frecuencias equilibran las dos facturas (como aquí), la diferencia
es de un dígito porcentual y hay que decirlo con esa cifra.