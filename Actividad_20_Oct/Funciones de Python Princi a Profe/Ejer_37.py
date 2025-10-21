#---------------------------------------------------------------
# Ejercicio 37 — ordenar_lista(lst, reverse=False)
#---------------------------------------------------------------

def ordenar_lista(lst, reverse=False):
    # Retorna nueva lista ordenada; no modifica original
    return sorted(lst, reverse=reverse)

if __name__ == "__main__":
    print(ordenar_lista([3,1,2]))         # [1,2,3]
    print(ordenar_lista([3,1,2], True))   # [3,2,1]
