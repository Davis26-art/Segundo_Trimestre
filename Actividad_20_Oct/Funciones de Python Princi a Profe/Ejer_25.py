#---------------------------------------------------------------
# Ejercicio 25 — capitalizar_palabras(s)
#---------------------------------------------------------------

def capitalizar_palabras(s):
    # Capitaliza cada palabra
    return ' '.join(word.capitalize() for word in s.split())

if __name__ == "__main__":
    print(capitalizar_palabras("hola mundo desde python"))  # 'Hola Mundo Desde Python'
