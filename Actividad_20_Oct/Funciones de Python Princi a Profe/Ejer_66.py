#---------------------------------------------------------------
# Ejercicio 66 — invertir_numero(n)
#---------------------------------------------------------------

def invertir_numero(n):
    # Invierte el orden de los dígitos de un número entero
    signo = -1 if n < 0 else 1
    return signo * int(str(abs(n))[::-1])

if __name__ == "__main__":
    print(invertir_numero(1234))  # 4321
