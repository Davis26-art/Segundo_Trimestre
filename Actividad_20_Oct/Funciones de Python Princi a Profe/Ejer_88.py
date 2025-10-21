#---------------------------------------------------------------
# Ejercicio 88 — contar_consonantes(cadena)
#---------------------------------------------------------------

def contar_consonantes(cadena):
    # Cuenta consonantes en la cadena
    return sum(1 for c in cadena.lower() if c.isalpha() and c not in "aeiou")

if __name__ == "__main__":
    print(contar_consonantes("Python"))  # 4
