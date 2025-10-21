# --------------------
# Ejercicio 19
# Clase RegistroTemperaturas: guarda temperaturas y devuelve la máxima.
# --------------------
class RegistroTemp19:
    """Registro de temperaturas con insert y consulta de máxima/minima/avg."""
    def __init__(self):
        self.temps = []

    def agregar(self, t):
        self.temps.append(float(t))
        return True

    def maxima(self):
        return max(self.temps) if self.temps else None

    def minima(self):
        return min(self.temps) if self.temps else None

    def promedio(self):
        return sum(self.temps)/len(self.temps) if self.temps else None

# Prueba del ejercicio 19
rt = RegistroTemp19()
rt.agregar(20); rt.agregar(25); rt.agregar(22)
print("E19 max,min,avg:", rt.maxima(), rt.minima(), round(rt.promedio(),2))