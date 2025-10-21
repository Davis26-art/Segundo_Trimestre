import random

# --------------------
# Ejercicio 79
# Clase SensorMovimiento con detección aleatoria.
# --------------------
class SensorMovimiento79:
    """Sensor que detecta movimiento (aleatorio True/False)."""
    def detectar(self):
        return random.choice([True, False])

# Prueba del ejercicio 79
sm = SensorMovimiento79()
print("E79 movimiento:", sm.detectar())

