import random

# --------------------
# Ejercicio 81
# Clase SensorTemperatura con lectura promedio.
# --------------------
class SensorTemperatura81:
    """Sensor que acumula lecturas y calcula promedio."""
    def __init__(self):
        self.valores = []

    def medir(self):
        val = random.uniform(20,30)
        self.valores.append(val)
        return val

    def promedio(self):
        return sum(self.valores)/len(self.valores)

# Prueba del ejercicio 81
st = SensorTemperatura81()
for _ in range(3): st.medir()
print("E81 promedio temp:", round(st.promedio(),2))