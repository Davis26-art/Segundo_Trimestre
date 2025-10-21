#---------------------------------------------------------------
# Ejercicio 13 — factorial_recursivo(n)
#---------------------------------------------------------------

def factorial_recursivo(n):
    # Calcula factorial con recursión
    if n < 0:
        raise ValueError("n debe ser >= 0")
    if n in (0, 1):
        return 1
    return n * factorial_recursivo(n - 1)

if __name__ == "__main__":
    print("6! ->", factorial_recursivo(6))  # 720
