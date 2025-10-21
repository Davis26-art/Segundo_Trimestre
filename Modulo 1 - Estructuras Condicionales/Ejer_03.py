# =========================================
# ANALIZADOR DE DATOS (SIN LIBRERÍAS EXTERNAS)
# =========================================

import random

# Creamos una lista de datos aleatorios
datos = [random.randint(10, 100) for _ in range(10)]

print("Datos generados:", datos)

# Calculamos el promedio
promedio = sum(datos) / len(datos)
print(f"Promedio de los datos: {promedio:.2f}")

# "Simulamos" el tipo de gráfico recomendado
if promedio < 40:
    print("Tipo de gráfico recomendado: 📊 Gráfico de Barras")
elif promedio < 70:
    print("Tipo de gráfico recomendado: 📈 Gráfico de Líneas")
else:
    print("Tipo de gráfico recomendado: 🥧 Gráfico Circular")

# Mostramos una representación simple del gráfico en texto
print("\nRepresentación visual (escala simbólica):")
for i, valor in enumerate(datos):
    print(f"Dato {i+1}: {'█' * (valor // 5)} ({valor})")
