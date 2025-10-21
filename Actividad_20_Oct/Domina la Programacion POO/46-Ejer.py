# --------------------
# Ejercicio 46
# Clase VehiculoCarga con capacidad de carga y método descargar/cargar.
# --------------------
class VehiculoCarga46:
    """Vehículo de carga con capacidad máxima y carga actual."""
    def __init__(self, capacidad):
        self.capacidad = float(capacidad)
        self.carga_actual = 0.0

    def cargar(self, cantidad):
        # añade sin exceder la capacidad
        if cantidad < 0:
            return False
        espacio = self.capacidad - self.carga_actual
        to_add = min(espacio, cantidad)
        self.carga_actual += to_add
        return to_add

    def descargar(self, cantidad):
        # quita sin bajar de 0
        if cantidad < 0:
            return False
        to_remove = min(self.carga_actual, cantidad)
        self.carga_actual -= to_remove
        return to_remove

# Prueba del ejercicio 46
vc = VehiculoCarga46(100)
print("E46 cargar 50 ->", vc.cargar(50), "carga_actual:", vc.carga_actual)
print("E46 descargar 30 ->", vc.descargar(30), "carga_actual:", vc.carga_actual)