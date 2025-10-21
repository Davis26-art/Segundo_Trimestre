import random

# --------------------
# Ejercicio 83
# Clase AlumnoPromedioAleatorio que genera notas aleatorias.
# --------------------
class Alumno83:
    """Alumno con generación aleatoria de notas y promedio."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = [random.randint(1,5) for _ in range(3)]

    def promedio(self):
        return sum(self.notas)/len(self.notas)

# Prueba del ejercicio 83
al = Alumno83("Laura")
print("E83 notas:", al.notas, "promedio:", al.promedio())
