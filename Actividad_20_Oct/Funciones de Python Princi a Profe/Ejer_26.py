#---------------------------------------------------------------
# Ejercicio 26 — contar_vocales(s)
#---------------------------------------------------------------

def contar_vocales(s):
    # Cuenta vocales (a,e,i,o,u) en minúsculas y mayúsculas
    vocales = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vocales)

if __name__ == "__main__":
    print("contar_vocales('Hola') ->", contar_vocales("Hola"))  # 2
