#---------------------------------------------------------------
# Ejercicio 18 — min_lista(lst)
#---------------------------------------------------------------

def min_lista(lst):
    # Retorna mínimo; asume lista no vacía
    if not lst:
        raise ValueError("lista vacía")
    return min(lst)

if __name__ == "__main__":
    print("min_lista([3,7,2]) ->", min_lista([3, 7, 2]))  # 2
