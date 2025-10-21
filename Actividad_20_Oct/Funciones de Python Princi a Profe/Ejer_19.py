#---------------------------------------------------------------
# Ejercicio 19 — promedio_lista(lst)
#---------------------------------------------------------------

def promedio_lista(lst):
    # Calcula promedio; retorna 0 si lista vacía
    if not lst:
        return 0
    return sum(lst) / len(lst)

if __name__ == "__main__":
    print("promedio_lista([4,5,6]) ->", promedio_lista([4,5,6]))  # 5.0
