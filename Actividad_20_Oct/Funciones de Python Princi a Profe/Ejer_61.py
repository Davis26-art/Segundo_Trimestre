#---------------------------------------------------------------
# Ejercicio 61 — par_o_impar()
#---------------------------------------------------------------

import random

def par_o_impar():
    # Genera número aleatorio y dice si es par o impar
    n = random.randint(1, 100)
    return n, "par" if n % 2 == 0 else "impar"

if __name__ == "__main__":
    print(par_o_impar())
