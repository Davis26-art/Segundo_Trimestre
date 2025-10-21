#---------------------------------------------------------------
# Ejercicio 98 — reemplazar_numeros_por_x(s)
#---------------------------------------------------------------

def reemplazar_numeros_por_x(s):
    # Sustituye los dígitos por 'X'
    return ''.join('X' if ch.isdigit() else ch for ch in s)

if __name__ == "__main__":
    print(reemplazar_numeros_por_x("Tel: 3001234567"))
