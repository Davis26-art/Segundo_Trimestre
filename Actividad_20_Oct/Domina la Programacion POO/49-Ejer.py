from Ejer_07 import Estudiante07

# --------------------
# Ejercicio 49
# Clase AlumnoRegistro que hereda Estudiante07 y añade id único autogenerado (simple).
# --------------------
class AlumnoRegistro(Estudiante07):
    """Alumno con id simple generado automáticamente incremental (clase variable)."""
    _contador = 1

    def __init__(self, nombre):
        super().__init__(nombre)
        self.id = AlumnoRegistro._contador
        AlumnoRegistro._contador += 1

# Prueba del ejercicio 49
ar1 = AlumnoRegistro("Luis")
ar2 = AlumnoRegistro("Sofia")
print("E49 ids:", ar1.id, ar2.id)