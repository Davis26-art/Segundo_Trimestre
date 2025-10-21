#---------------------------------------------------------------
# Ejercicio 47 — formatear_porcentaje(fraccion, decimals=2)
#---------------------------------------------------------------

def formatear_porcentaje(fraccion, decimals=2):
    # Convierte fracción a porcentaje formateado como string
    try:
        porcentaje = float(fraccion) * 100
    except (ValueError, TypeError):
        return "NaN"
    return f"{porcentaje:.{decimals}f}%"

if __name__ == "__main__":
    print(formatear_porcentaje(0.1234))  # '12.34%'
