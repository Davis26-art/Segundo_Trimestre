#---------------------------------------------------------------
# Ejercicio 54 — calcular_perimetro_circulo(radio)
#---------------------------------------------------------------

import math

def calcular_perimetro_circulo(radio):
    # Calcula el perímetro (circunferencia)
    return 2 * math.pi * radio

if __name__ == "__main__":
    print(calcular_perimetro_circulo(4))  # ≈ 25.13
