#---------------------------------------------------------------
# Ejercicio 82 — suma_cuadrados(lista)
#---------------------------------------------------------------

def suma_cuadrados(lista):
    # Suma de cuadrados de los elementos
    return sum(x**2 for x in lista)

if __name__ == "__main__":
    print(suma_cuadrados([1, 2, 3]))  # 14
