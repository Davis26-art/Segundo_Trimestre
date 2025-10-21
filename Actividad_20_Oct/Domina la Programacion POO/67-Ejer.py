from Ejer_07 import Estudiante07

# --------------------
# Ejercicio 67
# Clase EstudianteBeca que hereda Estudiante07 y añade monto beca.
# --------------------
class EstudianteBeca67(Estudiante07):
    """Extiende Estudiante con atributo monto de beca."""
    def __init__(self, nombre, beca):
        super().__init__(nombre)
        self.beca = beca

# Prueba del ejercicio 67
eb = EstudianteBeca67("María", 500000)
print("E67 beca:", eb.beca)