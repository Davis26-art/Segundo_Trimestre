#---------------------------------------------------------------
# 8. Ejercicio implícito — Alcance de variables
#---------------------------------------------------------------

x = 10  # variable global

def ejemplo():
    x = 5  # variable local
    print("Dentro de la función:", x)

ejemplo()
print("Fuera de la función:", x)
