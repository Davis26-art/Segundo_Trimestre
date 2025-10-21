#---------------------------------------------------------------
# Ejercicio 53 — calcular_area_circulo(radio)
#---------------------------------------------------------------

import math

def calcular_area_circulo(radio):
    # Calcula el área de un círculo
    return math.pi * radio ** 2

if __name__ == "__main__":
    print(calcular_area_circulo(4))  # ≈ 50.27
