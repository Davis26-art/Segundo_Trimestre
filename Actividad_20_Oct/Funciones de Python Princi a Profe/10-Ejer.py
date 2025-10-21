#---------------------------------------------------------------
# 10. Ejercicio implícito — Funciones anidadas
#---------------------------------------------------------------

def externa():
    def interna():
        print("Hola desde la función interna.")
    interna()  # se ejecuta dentro de la externa

externa()
