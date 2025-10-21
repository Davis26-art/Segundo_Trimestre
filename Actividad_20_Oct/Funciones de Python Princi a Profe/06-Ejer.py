
#---------------------------------------------------------------
# *6. Ejercicio implícito — args
#---------------------------------------------------------------

# Función que recibe cantidad indefinida de argumentos
def sumar(*numeros):
    total = sum(numeros)
    return total

# Ejemplo:
print(sumar(1, 2, 3, 4, 5))
