# --------------------
# Ejercicio 98
# Clase Bicicleta con marcha actual y método cambiar_marcha.
# --------------------
class Bicicleta98:
    """Bicicleta que cambia de marcha."""
    def __init__(self):
        self.marcha = 1

    def cambiar_marcha(self, nueva):
        if 1 <= nueva <= 6:
            self.marcha = nueva
        return self.marcha

# Prueba del ejercicio 98
b98 = Bicicleta98()
print("E98 cambiar marcha 3:", b98.cambiar_marcha(3))