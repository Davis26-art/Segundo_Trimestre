#---------------------------------------------------------------
# Ejercicio 34 — lista_unica(lst)
#---------------------------------------------------------------

def lista_unica(lst):
    # Retorna lista con elementos únicos (orden preservado)
    visto = set()
    res = []
    for x in lst:
        if x not in visto:
            res.append(x)
            visto.add(x)
    return res

if __name__ == "__main__":
    print(lista_unica([1,2,2,3,1]))  # [1,2,3]
