# --------------------
# Ejercicio 08
# Clase Empleado con sueldo base y método calcular salario con horas extras.
# --------------------
class Empleado08:
    """Empleado con salario base; horas extra pagan un multiplicador."""
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = float(salario_base)

    def salario_con_horas(self, horas_extra, tarifa_por_hora):
        # salario = base + horas_extra * tarifa
        if horas_extra < 0 or tarifa_por_hora < 0:
            return None
        return self.salario_base + horas_extra * tarifa_por_hora

# Prueba del ejercicio 08
emp = Empleado08("Andres", 1000)
print("E08 salario con 5h extra a 10:", emp.salario_con_horas(5, 10))