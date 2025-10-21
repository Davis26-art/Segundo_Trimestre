#---------------------------------------------------------------
# Ejercicio 6 — dividir_seguro(a,b)
#---------------------------------------------------------------

def dividir_seguro(a, b):
    # Retorna división o mensaje si divisor es 0
    if b == 0:
        return "Error: división por cero"
    return a / b

if __name__ == "__main__":
    print("dividir_seguro(10,2) ->", dividir_seguro(10, 2))  # 5.0
    print("dividir_seguro(10,0) ->", dividir_seguro(10, 0))  # Error...
