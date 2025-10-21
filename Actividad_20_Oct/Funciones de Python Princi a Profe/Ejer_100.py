#---------------------------------------------------------------
# Ejercicio 86 — nombre_completo(nombre, apellido)
#---------------------------------------------------------------

def nombre_completo(nombre, apellido):
    # Retorna nombre completo capitalizado
    return f"{nombre.capitalize()} {apellido.capitalize()}"

if __name__ == "__main__":
    print(nombre_completo("david","perez"))
