#---------------------------------------------------------------
# Ejercicio 84 — contar_mayores(lista, limite)
#---------------------------------------------------------------

def contar_mayores(lista, limite):
    # Cuenta cuántos valores superan un límite
    return sum(1 for x in lista if x > limite)

if __name__ == "__main__":
    print(contar_mayores([3, 7, 2, 10, 5], 5))  # 2
