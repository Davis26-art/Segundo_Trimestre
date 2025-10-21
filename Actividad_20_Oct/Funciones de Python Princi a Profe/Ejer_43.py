#---------------------------------------------------------------
# Ejercicio 43 — empieza_por_vocal(s)
#---------------------------------------------------------------

def empieza_por_vocal(s):
    # Comprueba si la primera letra es vocal
    if not s:
        return False
    return s[0].lower() in 'aeiou'

if __name__ == "__main__":
    print(empieza_por_vocal("Hola"))  # False
    print(empieza_por_vocal("Amigo")) # True
