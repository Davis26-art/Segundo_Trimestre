#---------------------------------------------------------------
# Ejercicio 30 — unir_palabras(lista, sep=" ")
#---------------------------------------------------------------

def unir_palabras(lista, sep=" "):
    # Une lista de palabras con separador sep
    return sep.join(lista)

if __name__ == "__main__":
    print(unir_palabras(["hola", "mundo"]))  # 'hola mundo'
