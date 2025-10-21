#---------------------------------------------------------------
# Ejercicio 95 — crear_diccionario_random(n)
#---------------------------------------------------------------

import random
import string

def crear_diccionario_random(n):
    # Crea diccionario con n pares letra->número random
    return {random.choice(string.ascii_uppercase): random.randint(1,100) for _ in range(n)}

if __name__ == "__main__":
    print(crear_diccionario_random(5))
