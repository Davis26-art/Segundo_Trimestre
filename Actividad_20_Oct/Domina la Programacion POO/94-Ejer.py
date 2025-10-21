# --------------------
# Ejercicio 94
# Clase PersonaSalario que calcula salario anual.
# --------------------
class PersonaSalario94:
    """Persona con salario mensual; calcula salario anual."""
    def __init__(self, nombre, salario_mensual):
        self.nombre = nombre
        self.salario_mensual = salario_mensual

    def salario_anual(self):
        return self.salario_mensual * 12

# Prueba del ejercicio 94
ps = PersonaSalario94("Diego", 1500000)
print("E94 anual:", ps.salario_anual())