# --------------------
# Ejercicio 69
# Clase Botella con capacidad y contenido.
# --------------------
class Botella69:
    """Botella con capacidad máxima y contenido actual."""
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.contenido = 0

    def llenar(self):
        self.contenido = self.capacidad
        return self.contenido

    def vaciar(self):
        self.contenido = 0
        return self.contenido

# Prueba del ejercicio 69
b69 = Botella69(1.5)
print("E69 llenar:", b69.llenar(), "vaciar:", b69.vaciar())