#---------------------------------------------------------------
# Ejercicio 12 — factorial_iterativo(n)
#---------------------------------------------------------------

def factorial_iterativo(n):
    # Calcula factorial de n iterativamente
    if n < 0:
        raise ValueError("n debe ser >= 0")
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

if __name__ == "__main__":
    print("5! ->", factorial_iterativo(5))  # 120
