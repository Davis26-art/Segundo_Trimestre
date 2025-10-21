# =========================================
# INVERTIR UNA CADENA SIN SLICING NI REVERSED
# =========================================

texto = "Python es divertido"
invertido = ""

for caracter in texto:
    invertido = caracter + invertido  # Va agregando al inicio

print(invertido)
