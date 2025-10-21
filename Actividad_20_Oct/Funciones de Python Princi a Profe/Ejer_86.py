#---------------------------------------------------------------
# Ejercicio 86 — es_vocal(letra)
#---------------------------------------------------------------

def es_vocal(letra):
    # True si la letra es vocal
    return letra.lower() in "aeiou"

if __name__ == "__main__":
    print(es_vocal('A'))  # True
