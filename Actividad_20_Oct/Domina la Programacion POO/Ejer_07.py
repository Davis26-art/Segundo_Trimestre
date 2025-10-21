# --------------------
# Ejercicio 07
# Clase Estudiante con lista de calificaciones; añadir y calcular promedio.
# --------------------
class Estudiante07:
    """Estudiante que guarda calificaciones y calcula promedio simple."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []  # lista vacía al inicio

    def agregar_nota(self, nota):
        # acepta notas entre 0 y 5 (ejemplo)
        if 0 <= nota <= 5:
            self.calificaciones.append(float(nota))
            return True
        return False

    def promedio(self):
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)

# Prueba del ejercicio 07
est = Estudiante07("Lucia")
est.agregar_nota(4.0)
est.agregar_nota(5.0)
print("E07 promedio:", est.promedio())