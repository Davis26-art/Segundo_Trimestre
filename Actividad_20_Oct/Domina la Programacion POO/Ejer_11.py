# --------------------
# Ejercicio 11
# Clase Mascota con nombre y especie; método describir.
# --------------------
class Mascota11:
    """Mascota básica: nombre y especie y método que devuelve descripción."""
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def describir(self):
        return f"{self.nombre} es un(a) {self.especie}."

# Prueba del ejercicio 11
m = Mascota11("Luna", "gato")
print("E11:", m.describir())