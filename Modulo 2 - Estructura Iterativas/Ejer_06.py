# =========================================
# SECUENCIA DE FIBONACCI CON WHILE
# =========================================

def fibonacci(n):
    secuencia = []
    a, b = 0, 1
    contador = 0

    while contador < n:
        secuencia.append(a)
        a, b = b, a + b
        contador += 1

    return secuencia

# Bloque de prueba
print(f"Primeros 10 números de Fibonacci: {fibonacci(10)}")
