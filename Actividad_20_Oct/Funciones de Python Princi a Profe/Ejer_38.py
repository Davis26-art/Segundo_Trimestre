#---------------------------------------------------------------
# Ejercicio 38 — contar_letras(s, letra)
#---------------------------------------------------------------

def contar_letras(s, letra):
    # Cuenta cuántas veces aparece 'letra' en 's'
    return s.count(letra)

if __name__ == "__main__":
    print(contar_letras("banana", "a"))  # 3
