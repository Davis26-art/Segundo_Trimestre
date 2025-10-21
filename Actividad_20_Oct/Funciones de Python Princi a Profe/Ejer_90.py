#---------------------------------------------------------------
# Ejercicio 90 — es_mayuscula(cadena)
#---------------------------------------------------------------

def es_mayuscula(cadena):
    # True si toda la cadena está en mayúsculas
    return cadena.isupper()

if __name__ == "__main__":
    print(es_mayuscula("HOLA"))  # True
