#---------------------------------------------------------------
# 2. Ejercicio Guiado 1 — Función Es Par
#---------------------------------------------------------------

# Función que determina si un número es par
def es_par(n):
    # El operador % devuelve el residuo de la división
    return n % 2 == 0

# Ejemplo de prueba
numero = 8
if es_par(numero):
    print(f"{numero} es par.")
else:
    print(f"{numero} es impar.")
