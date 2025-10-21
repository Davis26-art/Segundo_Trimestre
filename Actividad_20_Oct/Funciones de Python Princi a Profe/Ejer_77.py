#---------------------------------------------------------------
# Ejercicio 77 — media_lista_aleatoria()
#---------------------------------------------------------------

import random

def media_lista_aleatoria():
    # Genera lista aleatoria y calcula promedio
    lista = [random.randint(1, 100) for _ in range(10)]
    return lista, sum(lista) / len(lista)

if __name__ == "__main__":
    print(media_lista_aleatoria())
