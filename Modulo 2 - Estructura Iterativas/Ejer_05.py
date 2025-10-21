# =========================================
# TABLA DE MULTIPLICAR DEL 1 AL 10
# =========================================

print("Tabla de multiplicar del 1 al 10:")
print("-" * 40)

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")  # Espaciado uniforme
    print()  # Salto de línea al final de cada fila
