#---------------------------------------------------------------
# Ejercicio 96 — sumar_valores_diccionario(dic)
#---------------------------------------------------------------

def sumar_valores_diccionario(dic):
    # Suma los valores (numéricos)
    return sum(dic.values())

if __name__ == "__main__":
    print(sumar_valores_diccionario({'a':3,'b':7,'c':10}))  # 20
