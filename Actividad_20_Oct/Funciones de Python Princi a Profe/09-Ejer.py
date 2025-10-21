#---------------------------------------------------------------
# 9. Ejercicio implícito — Uso de global
#---------------------------------------------------------------

x = 10

def modificar_global():
    global x
    x = 20

modificar_global()
print("Nuevo valor global de x:", x)
