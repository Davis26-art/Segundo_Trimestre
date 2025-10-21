#---------------------------------------------------------------
# Ejercicio 67 — convertir_a_binario(n)
#---------------------------------------------------------------

def convertir_a_binario(n):
    # Retorna representación binaria del entero
    return bin(n)[2:]

if __name__ == "__main__":
    print(convertir_a_binario(10))  # '1010'
