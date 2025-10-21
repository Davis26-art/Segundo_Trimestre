# --------------------
# Ejercicio 58
# Clase Estacionamiento que calcula pago por horas.
# --------------------
class Estacionamiento58:
    """Calcula el costo de estacionamiento según horas y tarifa."""
    def __init__(self, tarifa_hora):
        self.tarifa_hora = tarifa_hora

    def calcular_pago(self, horas):
        return horas * self.tarifa_hora

# Prueba del ejercicio 58
e = Estacionamiento58(2000)
print("E58 pago por 3h:", e.calcular_pago(3))