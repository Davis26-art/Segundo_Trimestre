# --------------------
# Ejercicio 82
# Clase Animal con sonido personalizado.
# --------------------
class Animal82:
    """Animal con nombre y sonido."""
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def hablar(self):
        return f"{self.nombre} dice {self.sonido}"

# Prueba del ejercicio 82
a82 = Animal82("Perro", "guau")
print("E82:", a82.hablar())