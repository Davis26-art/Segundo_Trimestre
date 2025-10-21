#---------------------------------------------------------------
# Ejercicio 74 — mayusculas_aleatorias(cadena)
#---------------------------------------------------------------

import random

def mayusculas_aleatorias(cadena):
    # Convierte aleatoriamente letras a mayúsculas
    resultado = ""
    for ch in cadena:
        if ch.isalpha():
            resultado += ch.upper() if random.choice([True, False]) else ch.lower()
        else:
            resultado += ch
    return resultado

if __name__ == "__main__":
    print(mayusculas_aleatorias("python divertido"))
