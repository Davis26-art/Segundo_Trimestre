#---------------------------------------------------------------
# Ejercicio 59 — es_divisible(a, b)
#---------------------------------------------------------------

def es_divisible(a, b):
    # Devuelve True si a es divisible entre b
    if b == 0:
        return False
    return a % b == 0

if __name__ == "__main__":
    print(es_divisible(10, 5))  # True
    print(es_divisible(10, 3))  # False
