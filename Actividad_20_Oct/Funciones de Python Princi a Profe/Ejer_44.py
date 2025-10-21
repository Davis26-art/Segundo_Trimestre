#---------------------------------------------------------------
# Ejercicio 44 — termina_por_consonante(s)
#---------------------------------------------------------------

def termina_por_consonante(s):
    # True si el último carácter es consonante (ASCII letters)
    if not s:
        return False
    ch = s[-1].lower()
    return ch.isalpha() and ch not in 'aeiou'

if __name__ == "__main__":
    print(termina_por_consonante("casa"))  # False (a)
    print(termina_por_consonante("sol"))   # True (l)
