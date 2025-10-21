#---------------------------------------------------------------
# Ejercicio 80 — promedio_ponderado(lista_notas, lista_pesos)
#---------------------------------------------------------------

def promedio_ponderado(lista_notas, lista_pesos):
    # Calcula promedio ponderado entre notas y pesos
    if len(lista_notas) != len(lista_pesos) or not lista_notas:
        return 0
    total = sum(n * p for n, p in zip(lista_notas, lista_pesos))
    return total / sum(lista_pesos)

if __name__ == "__main__":
    print(promedio_ponderado([3, 4, 5], [2, 3, 5]))  # 4.3
