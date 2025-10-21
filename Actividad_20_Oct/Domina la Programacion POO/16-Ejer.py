# --------------------
# Ejercicio 16
# Clase TimerConEstado con encendido/apagado (booleano).
# --------------------
class Timer16:
    """Objeto con estado 'activo' encendido/apagado y control simple."""
    def __init__(self):
        self.activo = False

    def encender(self):
        self.activo = True
        return self.activo

    def apagar(self):
        self.activo = False
        return self.activo

# Prueba del ejercicio 16
tm = Timer16()
print("E16 encender:", tm.encender(), "apagar:", tm.apagar())