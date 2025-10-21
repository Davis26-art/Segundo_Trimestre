# --------------------
# Ejercicio 52
# Clase Fruta con nombre y color; método describir.
# --------------------
class Fruta52:
    """Fruta con atributos nombre y color, y método que la describe."""
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def describir(self):
        return f"La fruta {self.nombre} es de color {self.color}."

# Prueba del ejercicio 52
f = Fruta52("Manzana", "roja")
print("E52:", f.describir())