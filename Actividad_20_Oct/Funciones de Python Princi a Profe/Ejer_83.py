#---------------------------------------------------------------
# Ejercicio 83 — producto_lista(lista)
#---------------------------------------------------------------

def producto_lista(lista):
    # Multiplica todos los elementos
    producto = 1
    for x in lista:
        producto *= x
    return producto

if __name__ == "__main__":
    print(producto_lista([1, 2, 3, 4]))  # 24
