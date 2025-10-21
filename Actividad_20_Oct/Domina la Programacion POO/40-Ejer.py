# --------------------
# Ejercicio 40
# Clase Sensor con lectura y método validar rango.
# --------------------
class Sensor40:
    """Sensor con lectura y método para verificar si la lectura está en rango permitido."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.lectura = 0.0

    def actualizar(self, valor):
        self.lectura = float(valor)
        return self.lectura

    def en_rango(self, minimo, maximo):
        return minimo <= self.lectura <= maximo

# Prueba del ejercicio 40
s40 = Sensor40("Temp")
s40.actualizar(25.5)
print("E40 en rango 20-30:", s40.en_rango(20,30))