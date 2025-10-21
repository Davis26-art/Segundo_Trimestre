# =========================================
# FACTORIAL USANDO BUCLE WHILE
# =========================================

def factorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
    return resultado

# Bloque de prueba
numero = 5
print(f"El factorial de {numero} es: {factorial(numero)}")
