# --------------------
# Ejercicio 96
# Clase Clima con atributos temperatura y estado.
# --------------------
class Clima96:
    """Clima con temperatura y estado del cielo."""
    def __init__(self, temp, estado):
        self.temp = temp
        self.estado = estado

    def descripcion(self):
        return f"{self.estado} y {self.temp}°C"

# Prueba del ejercicio 96
cl = Clima96(28, "soleado")
print("E96:", cl.descripcion())