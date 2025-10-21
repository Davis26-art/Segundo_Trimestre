#---------------------------------------------------------------
# Ejercicio 91 — es_minuscula(cadena)
#---------------------------------------------------------------

def es_minuscula(cadena):
    # True si toda la cadena está en minúsculas
    return cadena.islower()

if __name__ == "__main__":
    print(es_minuscula("hola"))  # True
