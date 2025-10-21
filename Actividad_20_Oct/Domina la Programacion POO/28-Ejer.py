from Ejer_07 import Estudiante07

# --------------------
# Ejercicio 28
# Clase Profesor con asignatura y método para asignar nota a estudiante (simple, sin validación de relación).
# --------------------
class Profesor28:
    """Profesor que puede asignar nota a cualquier objeto Estudiante que tenga atributo 'calificaciones'."""
    def __init__(self, nombre, asignatura):
        self.nombre = nombre
        self.asignatura = asignatura

    def poner_nota(self, estudiante, nota):
        if hasattr(estudiante, "agregar_nota"):
            return estudiante.agregar_nota(nota)
        return False

# Prueba del ejercicio 28
prof = Profesor28("Luis", "Matemáticas")
est2 = Estudiante07("Carlos")
print("E28 poner nota 4:", prof.poner_nota(est2, 4), "promedio:", est2.promedio())