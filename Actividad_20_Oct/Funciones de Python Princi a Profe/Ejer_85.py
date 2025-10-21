#---------------------------------------------------------------
# Ejercicio 85 — generar_password(longitud)
#---------------------------------------------------------------

import random
import string

def generar_password(longitud=8):
    # Genera contraseña aleatoria con letras y dígitos
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))

if __name__ == "__main__":
    print(generar_password())
