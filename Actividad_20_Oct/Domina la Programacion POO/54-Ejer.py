# --------------------
# Ejercicio 54
# Clase Auto con combustible y métodos para conducir y recargar.
# --------------------
class Auto54:
    """Auto con nivel de combustible (litros) y métodos para conducir y recargar."""
    def __init__(self, combustible):
        self.combustible = combustible

    def conducir(self, km):
        # cada 10 km consume 1 litro
        consumo = km / 10
        if consumo <= self.combustible:
            self.combustible -= consumo
            return True
        return False

    def recargar(self, litros):
        self.combustible += litros
        return self.combustible

# Prueba del ejercicio 54
a = Auto54(5)
print("E54 conducir 30km ->", a.conducir(30), "combustible:", round(a.combustible,2))
print("E54 recargar 3L ->", a.recargar(3))