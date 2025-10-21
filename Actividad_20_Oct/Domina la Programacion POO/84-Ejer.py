# --------------------
# Ejercicio 84
# Clase TemporizadorProgreso que muestra porcentaje completado.
# --------------------
class Temporizador84:
    """Temporizador que avanza en porcentaje hasta 100%."""
    def __init__(self):
        self.progreso = 0

    def avanzar(self, pct):
        self.progreso = min(100, self.progreso + pct)
        return self.progreso

# Prueba del ejercicio 84
tp = Temporizador84()
print("E84 avanzar 30:", tp.avanzar(30))