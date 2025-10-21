#---------------------------------------------------------------
# 5. Ejercicio implícito — Valores por defecto
#---------------------------------------------------------------

# Función con parámetro con valor por defecto
def saludar(nombre="invitado"):
    print(f"Hola {nombre}, ¡bienvenido!")

# Ejemplos:
saludar("Laura")   # usa el argumento dado
saludar()          # usa el valor por defecto


