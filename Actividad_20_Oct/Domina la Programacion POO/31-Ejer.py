from Ejer_05 import Vehiculo05

# --------------------
# Ejercicio 31
# Clase VehiculoElectrico que hereda de Vehiculo05 y añade nivel batería.
# --------------------
class VehiculoElectrico31(Vehiculo05):
    """Vehículo eléctrico con nivel de batería (0-100)."""
    def __init__(self, marca, modelo, bateria=100):
        super().__init__(marca, modelo)
        self.bateria = bateria

    def consumir_bateria(self, porcentaje):
        # reduce batería sin bajar de 0
        self.bateria = max(0, self.bateria - porcentaje)
        return self.bateria

# Prueba del ejercicio 31
ve = VehiculoElectrico31("Tesla", "Model 3", 80)
print("E31 bateria antes:", ve.bateria, "después -10:", ve.consumir_bateria(10))