# --------------------
# Ejercicio 41
# Clase Habitacion con area, capacidad y método puede_entrar(n_personas)
# --------------------
class Habitacion41:
    """Habitación con área (m2) y capacidad máxima de personas."""
    def __init__(self, nombre, area, capacidad):
        self.nombre = nombre
        self.area = area
        self.capacidad = capacidad

    def puede_entrar(self, personas):
        return personas <= self.capacidad

# Prueba del ejercicio 41
h = Habitacion41("Sala", 20, 5)
print("E41 puede 4?", h.puede_entrar(4), "puede 6?", h.puede_entrar(6))