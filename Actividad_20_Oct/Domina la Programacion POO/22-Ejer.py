# --------------------
# Ejercicio 22
# Clase Piloto con horas de vuelo; puede agregar horas y verificar si cumple X horas.
# --------------------
class Piloto22:
    """Piloto que acumula horas de vuelo y verifica si cumple mínimo."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.horas_vuelo = 0

    def agregar_horas(self, h):
        if h > 0:
            self.horas_vuelo += h
            return True
        return False

    def cumple_minimo(self, minimo):
        return self.horas_vuelo >= minimo

# Prueba del ejercicio 22
pil = Piloto22("Miguel")
pil.agregar_horas(120)
print("E22 cumple 100h?", pil.cumple_minimo(100))