#---------------------------------------------------------------
# 3. Extensión del Ejercicio Guiado — Función Es Impar
#---------------------------------------------------------------

# Función complementaria para determinar si un número es impar
def es_impar(n):
    return n % 2 != 0

# Ejemplo de prueba
numero = 7
if es_impar(numero):
    print(f"{numero} es impar.")
else:
    print(f"{numero} es par.")

