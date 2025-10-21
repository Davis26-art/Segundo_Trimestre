import random

# --------------------
# Ejercicio 68
# Clase SensorHumedad con lectura aleatoria entre 0 y 100.
# --------------------
class SensorHumedad68:
    """Sensor de humedad que simula lectura entre 0 y 100%."""
    def medir(self):
        return random.randint(0, 100)

# Prueba del ejercicio 68
sh = SensorHumedad68()
print("E68 humedad:", sh.medir())