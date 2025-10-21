#---------------------------------------------------------------
# Ejercicio 73 — es_multiple(a,b)
#---------------------------------------------------------------

def es_multiple(a, b):
    # True si a es múltiplo de b
    if b == 0:
        return False
    return a % b == 0

if __name__ == "__main__":
    print(es_multiple(12, 4))  # True
