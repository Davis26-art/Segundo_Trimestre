#---------------------------------------------------------------
# Ejercicio 11 — saludo_default(nombre="invitado")
#---------------------------------------------------------------

def saludo_default(nombre="invitado"):
    # Saluda usando valor por defecto si no se pasa nombre
    return f"Hola, {nombre}!"

if __name__ == "__main__":
    print(saludo_default("Laura"))  # Hola, Laura!
    print(saludo_default())         # Hola, invitado!
