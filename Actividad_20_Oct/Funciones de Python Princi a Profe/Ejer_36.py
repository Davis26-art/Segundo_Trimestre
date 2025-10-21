#---------------------------------------------------------------
# Ejercicio 36 — invertir_lista(lst)
#---------------------------------------------------------------

# 36_invertir_lista.py
def invertir_lista(lst):
    # Retorna copia invertida de la lista
    return lst[::-1]

if __name__ == "__main__":
    print(invertir_lista([1,2,3]))  # [3,2,1]
