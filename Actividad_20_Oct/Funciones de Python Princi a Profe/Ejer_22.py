#---------------------------------------------------------------
# Ejercicio 22 — es_palindromo(s)
#---------------------------------------------------------------

def es_palindromo(s):
    # Comprueba si s es palíndromo ignorando espacios y case
    s_clean = ''.join(s.split()).lower()
    return s_clean == s_clean[::-1]

if __name__ == "__main__":
    print("es_palindromo('Anita lava la tina') ->", es_palindromo("Anita lava la tina"))  # True
