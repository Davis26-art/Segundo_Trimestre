# --------------------
# Ejercicio 43
# Clase ProfesorMagico con método estático que da saludo general (uso de @staticmethod).
# --------------------
class Profesor43:
    """Profesor con método estático para saludo institucional."""
    def __init__(self, nombre):
        self.nombre = nombre

    @staticmethod
    def saludo_institucional():
        return "Bienvenidos al curso"

# Prueba del ejercicio 43
print("E43 saludo institucional:", Profesor43.saludo_institucional())