# =========================================
# CALCULADORA DE IMC (Índice de Masa Corporal)
# =========================================

# Pedimos los datos al usuario
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calculamos el IMC
imc = peso / (altura ** 2)

# Clasificamos el resultado
if imc < 18.5:
    print(f"Tu IMC es {imc:.2f} - Clasificación: Bajo peso")
elif imc < 25:
    print(f"Tu IMC es {imc:.2f} - Clasificación: Peso normal")
elif imc < 30:
    print(f"Tu IMC es {imc:.2f} - Clasificación: Sobrepeso")
else:
    print(f"Tu IMC es {imc:.2f} - Clasificación: Obesidad")
