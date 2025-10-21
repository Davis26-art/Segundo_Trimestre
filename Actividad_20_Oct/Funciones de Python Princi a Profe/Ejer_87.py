#---------------------------------------------------------------
# Ejercicio 87 — es_consonante(letra)
#---------------------------------------------------------------

def es_consonante(letra):
    # True si es letra y no vocal
    return letra.isalpha() and letra.lower() not in "aeiou"

if __name__ == "__main__":
    print(es_consonante('b'))  # True
