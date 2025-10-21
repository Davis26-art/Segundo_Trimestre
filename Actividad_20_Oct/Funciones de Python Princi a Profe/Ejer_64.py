#---------------------------------------------------------------
# Ejercicio 64 — contar_impares(lista)
#---------------------------------------------------------------

def contar_impares(lista):
    # Cuenta cuántos números impares hay
    return len([x for x in lista if x % 2 != 0])

if __name__ == "__main__":
    print(contar_impares([1, 2, 3, 4, 5, 6]))  # 3
