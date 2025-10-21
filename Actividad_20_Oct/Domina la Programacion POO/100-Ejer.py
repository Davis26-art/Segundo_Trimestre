# --------------------
# Ejercicio 100
# Clase Cuentakilometros que acumula distancia recorrida.
# --------------------
class Cuentakilometros100:
    """Contador de kilómetros de un vehículo."""
    def __init__(self):
        self.km = 0

    def recorrer(self, km):
        self.km += km
        return self.km

# Prueba del ejercicio 100
ck = Cuentakilometros100()
print("E100 recorrer 15km:", ck.recorrer(15))