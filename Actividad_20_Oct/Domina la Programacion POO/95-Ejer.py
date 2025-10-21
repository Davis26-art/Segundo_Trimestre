# --------------------
# Ejercicio 95
# Clase ControlPuerta con abrir/cerrar.
# --------------------
class ControlPuerta95:
    """Puerta con estado abierta/cerrada."""
    def __init__(self):
        self.abierta = False

    def abrir(self):
        self.abierta = True
        return self.abierta

    def cerrar(self):
        self.abierta = False
        return self.abierta

# Prueba del ejercicio 95
p95 = ControlPuerta95()
print("E95 abrir:", p95.abrir(), "cerrar:", p95.cerrar())