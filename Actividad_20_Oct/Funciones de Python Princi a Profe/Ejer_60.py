#---------------------------------------------------------------
# Ejercicio 60 — numero_aleatorio(limite)
#---------------------------------------------------------------

import random

def numero_aleatorio(limite):
    # Genera número aleatorio entre 1 y límite
    return random.randint(1, limite)

if __name__ == "__main__":
    print(numero_aleatorio(10))
