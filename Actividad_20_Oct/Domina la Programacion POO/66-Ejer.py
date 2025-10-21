# --------------------
# Ejercicio 66
# Clase HabitacionHotel con ocupada/libre.
# --------------------
class Habitacion66:
    """Habitación de hotel con estado de ocupación."""
    def __init__(self, numero):
        self.numero = numero
        self.ocupada = False

    def ocupar(self):
        self.ocupada = True
        return True

    def liberar(self):
        self.ocupada = False
        return True

# Prueba del ejercicio 66
hab = Habitacion66(101)
print("E66 ocupar:", hab.ocupar(), "liberar:", hab.liberar())