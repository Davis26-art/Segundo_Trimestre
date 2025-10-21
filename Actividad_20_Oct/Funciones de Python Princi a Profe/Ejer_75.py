#---------------------------------------------------------------
# Ejercicio 75 — adivinar_numero()
#---------------------------------------------------------------

import random

def adivinar_numero():
    # Juego simple: adivinar número del 1 al 5
    secreto = random.randint(1, 5)
    intento = random.randint(1, 5)  # simulamos intento automático
    return f"Secreto: {secreto}, Intento: {intento}, {'¡Acertaste!' if intento == secreto else 'Fallaste'}"

if __name__ == "__main__":
    print(adivinar_numero())
