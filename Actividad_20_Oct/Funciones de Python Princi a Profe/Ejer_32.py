#---------------------------------------------------------------
# Ejercicio 32 — quitar_espacios(s)
#---------------------------------------------------------------

def quitar_espacios(s):
    # Quita espacios al inicio y fin
    return s.strip()

if __name__ == "__main__":
    print(">" + quitar_espacios("  hola  ") + "<")  # '>hola<'
