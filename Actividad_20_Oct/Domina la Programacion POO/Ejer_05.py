# --------------------
# Ejercicio 05
# Clase Vehiculo con marca, modelo, velocidad; métodos acelerar y frenar.
# --------------------
class Vehiculo05:
    """Vehículo simple: controla velocidad con aceleraciones y frenadas (sin unidad)."""
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0  # velocidad inicial

    def acelerar(self, incremento):
        # incremento positivo aumenta la velocidad
        if incremento > 0:
            self.velocidad += incremento
        return self.velocidad

    def frenar(self, decremento):
        # frena y evita velocidad negativa
        if decremento > 0:
            self.velocidad = max(0, self.velocidad - decremento)
        return self.velocidad

# Prueba del ejercicio 05
v = Vehiculo05("Toyota", "Corolla")
print("E05 acelerar 50 ->", v.acelerar(50))
print("E05 frenar 20 ->", v.frenar(20))