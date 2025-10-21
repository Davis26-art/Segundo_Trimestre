# --------------------
# Ejercicio 71
# Clase CocheAlquiler con tarifa por día y método calcular costo.
# --------------------
class CocheAlquiler71:
    """Coche de alquiler que calcula costo según días."""
    def __init__(self, tarifa_dia):
        self.tarifa_dia = tarifa_dia

    def calcular_costo(self, dias):
        return dias * self.tarifa_dia

# Prueba del ejercicio 71
c71 = CocheAlquiler71(50000)
print("E71 costo 3 días:", c71.calcular_costo(3))