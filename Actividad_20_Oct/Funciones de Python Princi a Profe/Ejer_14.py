#---------------------------------------------------------------
# Ejercicio 14 — fibonacci(n)
#---------------------------------------------------------------

def fibonacci(n):
    # Retorna el n-ésimo número de Fibonacci (0-indexado)
    if n < 0:
        raise ValueError("n debe ser >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    print("Fibo(7) ->", fibonacci(7))  # 13
