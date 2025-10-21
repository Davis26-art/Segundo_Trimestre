# --------------------
# Ejercicio 76
# Clase CajaFuerte con contraseña numérica.
# --------------------
class CajaFuerte76:
    """Caja fuerte con código numérico y verificación."""
    def __init__(self, codigo):
        self.codigo = codigo
        self.abierta = False

    def abrir(self, intento):
        self.abierta = intento == self.codigo
        return self.abierta

# Prueba del ejercicio 76
cf = CajaFuerte76(1234)
print("E76 abrir 0000:", cf.abrir(0000), "abrir 1234:", cf.abrir(1234))