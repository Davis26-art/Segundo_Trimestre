#---------------------------------------------------------------
# Ejercicio 99 — validar_contraseña(password)
#---------------------------------------------------------------

def validar_contraseña(password):
    # Contraseña válida si tiene al menos 8 caracteres y un número
    tiene_numero = any(ch.isdigit() for ch in password)
    return len(password) >= 8 and tiene_numero

if __name__ == "__main__":
    print(validar_contraseña("clave123"))  # True
