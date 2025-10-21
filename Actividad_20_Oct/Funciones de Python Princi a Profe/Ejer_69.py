#---------------------------------------------------------------
# Ejercicio 69 — contar_digitos(n)
#---------------------------------------------------------------

def contar_digitos(n):
    # Retorna cantidad de dígitos de un número
    return len(str(abs(n)))

if __name__ == "__main__":
    print(contar_digitos(12345))  # 5
