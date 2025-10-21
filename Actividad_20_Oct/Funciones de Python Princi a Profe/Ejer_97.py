#---------------------------------------------------------------
# Ejercicio 97 — invertir_diccionario(dic)
#---------------------------------------------------------------

def invertir_diccionario(dic):
    # Intercambia claves y valores
    return {v: k for k, v in dic.items()}

if __name__ == "__main__":
    print(invertir_diccionario({'a':1,'b':2}))  # {1:'a',2:'b'}
