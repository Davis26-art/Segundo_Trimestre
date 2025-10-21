# --------------------
# Ejercicio 55
# Clase Lámpara con estado encendida/apagada.
# --------------------
class Lampara55:
    """Lámpara que puede encenderse y apagarse."""
    def __init__(self):
        self.encendida = False

    def encender(self):
        self.encendida = True
        return self.encendida

    def apagar(self):
        self.encendida = False
        return self.encendida

# Prueba del ejercicio 55
l = Lampara55()
print("E55 encender:", l.encender(), "apagar:", l.apagar())