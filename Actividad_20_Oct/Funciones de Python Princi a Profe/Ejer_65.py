#---------------------------------------------------------------
# Ejercicio 65 — sumar_digitos(n)
#---------------------------------------------------------------

def sumar_digitos(n):
    # Suma los dígitos de un número entero positivo
    return sum(int(d) for d in str(abs(n)))

if __name__ == "__main__":
    print(sumar_digitos(12345))  # 15
