#---------------------------------------------------------------
# 12. Ejercicio implícito — Recursividad
#---------------------------------------------------------------

# Función recursiva para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo:
print("5! =", factorial(5))
