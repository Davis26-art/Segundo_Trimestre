from Ejer_07 import Estudiante07

# --------------------
# Ejercicio 38
# Clase AlumnoHereda de Estudiante07 que añade método aprobar (bool por nota).
# --------------------
class Alumno38(Estudiante07):
    """Alumno que puede determinar si aprobó con nota mínima dada."""
    def aprobado(self, minimo=3.0):
        return self.promedio() >= minimo

# Prueba del ejercicio 38
a38 = Alumno38("Pedro")
a38.agregar_nota(4); a38.agregar_nota(3)
print("E38 promedio:", a38.promedio(), "aprobado>=3?", a38.aprobado(3))