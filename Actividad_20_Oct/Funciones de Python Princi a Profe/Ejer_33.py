#---------------------------------------------------------------
# Ejercicio 33 — contar_palabras(s)
#---------------------------------------------------------------

def contar_palabras(s):
    # Cuenta palabras separadas por espacios
    return len(s.split())

if __name__ == "__main__":
    print(contar_palabras("hola mundo python"))  # 3
