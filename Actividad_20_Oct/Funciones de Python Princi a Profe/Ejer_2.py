#---------------------------------------------------------------
# Ejercicio 2 — es_impar(n)
#---------------------------------------------------------------

def es_impar(n):
    # True si n no es divisible entre 2
    return n % 2 != 0

if __name__ == "__main__":
    print("es_impar(4) ->", es_impar(4))  # False
    print("es_impar(7) ->", es_impar(7))  # True
