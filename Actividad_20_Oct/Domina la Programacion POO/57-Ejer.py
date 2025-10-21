import random

# --------------------
# Ejercicio 57
# Clase SensorLuz que mide intensidad (0–100).
# --------------------
class SensorLuz57:
    """Sensor de luz con valores entre 0 y 100."""
    def __init__(self):
        self.intensidad = 0

    def medir(self):
        self.intensidad = random.randint(0, 100)
        return self.intensidad

    def es_baja(self):
        return self.intensidad < 30

# Prueba del ejercicio 57
sl = SensorLuz57()
print("E57 intensidad:", sl.medir(), "baja?", sl.es_baja())