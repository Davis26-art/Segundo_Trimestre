#---------------------------------------------------------------
# Ejercicio 76 — generar_lista_aleatoria(n, minimo, maximo)
#---------------------------------------------------------------

import random

def generar_lista_aleatoria(n, minimo, maximo):
    # Genera lista de n números aleatorios entre mínimo y máximo
    return [random.randint(minimo, maximo) for _ in range(n)]

if __name__ == "__main__":
    print(generar_lista_aleatoria(5, 1, 10))
