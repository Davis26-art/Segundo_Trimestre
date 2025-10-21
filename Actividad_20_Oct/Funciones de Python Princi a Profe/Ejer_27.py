#---------------------------------------------------------------
# Ejercicio 27 — remover_vocales(s)
#---------------------------------------------------------------

def remover_vocales(s):
    # Quita vocales de la cadena
    vocales = "aeiouAEIOU"
    return ''.join(ch for ch in s if ch not in vocales)

if __name__ == "__main__":
    print(remover_vocales("Hola mundo"))  # 'Hl mnd'
