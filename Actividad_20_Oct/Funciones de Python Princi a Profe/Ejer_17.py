#---------------------------------------------------------------
# Ejercicio 17 — max_lista(lst)
#---------------------------------------------------------------

def max_lista(lst):
    # Retorna el máximo; asume lista no vacía
    if not lst:
        raise ValueError("lista vacía")
    return max(lst)

if __name__ == "__main__":
    print("max_lista([3,7,2]) ->", max_lista([3, 7, 2]))  # 7
