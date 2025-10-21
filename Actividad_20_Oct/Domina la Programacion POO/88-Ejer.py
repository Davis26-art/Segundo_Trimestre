import random

# --------------------
# Ejercicio 88
# Clase SensorPresion con rango de seguridad.
# --------------------
class SensorPresion88:
    """Sensor con presión y verificación de rango seguro."""
    def __init__(self):
        self.presion = 0

    def medir(self):
        self.presion = random.uniform(0.8, 1.2)
        return self.presion

    def segura(self):
        return 0.9 <= self.presion <= 1.1

# Prueba del ejercicio 88
sp = SensorPresion88()
sp.medir()
print("E88 presion:", round(sp.presion,2), "segura?", sp.segura())