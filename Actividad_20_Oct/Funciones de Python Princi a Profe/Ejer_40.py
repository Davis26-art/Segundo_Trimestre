#---------------------------------------------------------------
# Ejercicio 40 — iniciales(nombre_completo)
#---------------------------------------------------------------

def iniciales(nombre_completo):
    # Devuelve las iniciales separadas por puntos
    partes = nombre_completo.split()
    return '.'.join(p[0].upper() for p in partes) + '.'

if __name__ == "__main__":
    print(iniciales("David Pérez Gómez"))  # 'D.P.G.'
