#---------------------------------------------------------------
# Ejercicio 31 — reemplazar_caracter(s, viejo, nuevo)
#---------------------------------------------------------------

def reemplazar_caracter(s, viejo, nuevo):
    # Reemplaza todas las ocurrencias de viejo por nuevo
    return s.replace(viejo, nuevo)

if __name__ == "__main__":
    print(reemplazar_caracter("manzana", "a", "o"))  # 'monzono'
