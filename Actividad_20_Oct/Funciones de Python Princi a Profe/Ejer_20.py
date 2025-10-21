#---------------------------------------------------------------
# Ejercicio 20 — contar_ocurrencias(lst, x)
#---------------------------------------------------------------

def contar_ocurrencias(lst, x):
    # Cuenta cuántas veces aparece x en lst
    return lst.count(x)

if __name__ == "__main__":
    print("contar_ocurrencias([1,2,2,3],2) ->", contar_ocurrencias([1,2,2,3], 2))  # 2
