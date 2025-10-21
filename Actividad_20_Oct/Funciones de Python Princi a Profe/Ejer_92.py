#---------------------------------------------------------------
# Ejercicio 92 — es_numero(cadena)
#---------------------------------------------------------------

def es_numero(cadena):
    # True si la cadena representa un número
    return cadena.isdigit()

if __name__ == "__main__":
    print(es_numero("1234"))  # True
