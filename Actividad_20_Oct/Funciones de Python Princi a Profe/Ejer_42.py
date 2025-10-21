#---------------------------------------------------------------
# Ejercicio 42 — es_subcadena(s, sub)
#---------------------------------------------------------------

def es_subcadena(s, sub):
    # Devuelve True si 'sub' está dentro de 's'
    return sub in s

if __name__ == "__main__":
    print(es_subcadena("hola mundo", "mun"))  # True
