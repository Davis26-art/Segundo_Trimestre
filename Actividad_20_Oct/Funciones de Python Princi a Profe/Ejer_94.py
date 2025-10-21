#---------------------------------------------------------------
# Ejercicio 94 — suma_diagonal_matriz(matriz)
#---------------------------------------------------------------

def suma_diagonal_matriz(matriz):
    # Suma diagonal principal de matriz cuadrada
    return sum(matriz[i][i] for i in range(len(matriz)))

if __name__ == "__main__":
    print(suma_diagonal_matriz([[1,2,3],[4,5,6],[7,8,9]]))  # 15
