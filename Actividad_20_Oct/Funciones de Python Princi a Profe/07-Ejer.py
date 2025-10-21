#---------------------------------------------------------------
# 7. Ejercicio implícito — kwargs
#---------------------------------------------------------------

# Función que usa **kwargs para recibir argumentos nombrados
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

# Ejemplo:
mostrar_datos(nombre="Ana", edad=22, ciudad="Bogotá")

