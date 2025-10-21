#---------------------------------------------------------------
# Ejercicio 28 — es_anagrama(a,b)
#---------------------------------------------------------------

def es_anagrama(a, b):
    # Compara si dos cadenas son anagramas (ignorando espacios y case)
    a_clean = ''.join(a.split()).lower()
    b_clean = ''.join(b.split()).lower()
    return sorted(a_clean) == sorted(b_clean)

if __name__ == "__main__":
    print("es_anagrama('Roma','Amor') ->", es_anagrama("Roma", "Amor"))  # True
