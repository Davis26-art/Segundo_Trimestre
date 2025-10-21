#---------------------------------------------------------------
# Ejercicio 35 — elementos_comunes(a,b)
#---------------------------------------------------------------

def elementos_comunes(a, b):
    # Retorna la intersección entre dos listas (sin duplicados)
    return list(set(a) & set(b))

if __name__ == "__main__":
    print(elementos_comunes([1,2,3], [2,3,4]))  # [2,3] (orden no garantizado)
