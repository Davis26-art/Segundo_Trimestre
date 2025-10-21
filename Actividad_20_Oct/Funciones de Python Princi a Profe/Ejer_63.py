#---------------------------------------------------------------
# Ejercicio 63 — sumar_pares(lista)
#---------------------------------------------------------------

def sumar_pares(lista):
    # Suma solo los números pares de una lista
    return sum(x for x in lista if x % 2 == 0)

if __name__ == "__main__":
    print(sumar_pares([1, 2, 3, 4, 5, 6]))  # 12
