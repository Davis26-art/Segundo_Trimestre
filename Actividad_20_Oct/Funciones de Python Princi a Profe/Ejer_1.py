#---------------------------------------------------------------
# Ejercicio 1 — es_par(n)
#---------------------------------------------------------------

def es_par(n):
    # Devuelve True si n es divisible entre 2
    return n % 2 == 0

if __name__ == "__main__":
    print("es_par(4) ->", es_par(4))   # True
    print("es_par(7) ->", es_par(7))   # False
