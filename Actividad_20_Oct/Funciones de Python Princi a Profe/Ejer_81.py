#---------------------------------------------------------------
# Ejercicio 81 — mayor_diferencia(lista)
#---------------------------------------------------------------

def mayor_diferencia(lista):
    # Retorna diferencia entre máximo y mínimo
    if not lista:
        return 0
    return max(lista) - min(lista)

if __name__ == "__main__":
    print(mayor_diferencia([10, 2, 8, 20]))  # 18
