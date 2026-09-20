# Código base — Semana 04
# Fuente: 01-Momento-1-Contrato-y-secuencia/04-Semana-04-Arreglos-y-estructuras-estaticas/02-guia-de-laboratorio.html

import time
from lista_arreglo import ListaArreglo

N = 20_000

# Insertar SIEMPRE al final
lista = ListaArreglo()
inicio = time.perf_counter()
for i in range(N):
    lista.insertar(lista.tamaño(), i)
al_final = time.perf_counter() - inicio

# Insertar SIEMPRE al inicio
lista = ListaArreglo()
inicio = time.perf_counter()
for i in range(N):
    lista.insertar(0, i)
al_inicio = time.perf_counter() - inicio

print(f"{N:,} inserciones al final:  {al_final:7.3f} s")
print(f"{N:,} inserciones al inicio: {al_inicio:7.3f} s")
print(f"Al inicio es {al_inicio / al_final:.0f} veces más lento")

# Pregunta: si duplicas N, ¿cuánto esperas que crezca cada uno?
# Compruébalo.


# ---------------------------------------------------------------------
# Parte C — Medir las cinco operaciones con timeit
# Catálogos de 1.000, 10.000, 80.000 y 200.000 registros.
# Cada medición se repite REPETICIONES veces y se toma la mediana.
# ---------------------------------------------------------------------

import csv
import statistics
import timeit

TAMANOS = [1_000, 10_000, 80_000, 200_000]
REPETICIONES = 7          # mínimo exigido: 5


def construir(n):
    """Catálogo ordenado con n elementos: 0, 2, 4, ..., 2(n-1)."""
    catalogo = ListaArreglo()
    for i in range(n):
        catalogo.insertar(catalogo.tamaño(), 2 * i)
    return catalogo


# operación -> (sentencia a medir, veces que se ejecuta por muestra)
# Se mide el peor caso de cada una.
OPERACIONES = {
    "insertar":          ("lista.insertar(0, -1)", 1),          # al inicio
    "insertar_ordenado": ("lista.insertar_ordenado(-1)", 1),    # va al inicio
    "obtener":           ("lista.obtener(n // 2)", 10_000),
    "buscar_lineal":     ("lista.buscar_lineal(-1)", 10),       # no está
    "buscar_binaria":    ("lista.buscar_binaria(-1)", 10_000),  # no está
}

print("\n--- Parte C: mediana de", REPETICIONES, "repeticiones ---")
filas = []
for operacion, (sentencia, veces) in OPERACIONES.items():
    for n in TAMANOS:
        # El setup (construir el catálogo) no se cronometra.
        muestras = timeit.repeat(
            sentencia,
            setup="lista = construir(n)",
            globals={"construir": construir, "n": n},
            number=veces,
            repeat=REPETICIONES,
        )
        mediana = statistics.median(muestras) / veces   # segundos por operación
        filas.append((operacion, n, mediana))
        print(f"{operacion:<18} n={n:>7,}  {mediana:.3e} s")

with open("resultados.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["operacion", "n", "mediana_s"])
    escritor.writerows(filas)

# Gráfica: todas las operaciones superpuestas, escala log-log.
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Sin matplotlib no se genera la gráfica (pip install matplotlib).")
else:
    for operacion in OPERACIONES:
        puntos = [(n, t) for op, n, t in filas if op == operacion]
        plt.plot([p[0] for p in puntos], [p[1] for p in puntos],
                 marker="o", label=operacion)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Tamaño del catálogo n (escala logarítmica)")
    plt.ylabel("Tiempo por operación en segundos (escala logarítmica)")
    plt.title("ListaArreglo: tiempo por operación (peor caso)")
    plt.legend()
    plt.grid(True, which="both", alpha=0.3)
    plt.savefig("grafica.png", dpi=150)
    print("Escritos resultados.csv y grafica.png")
