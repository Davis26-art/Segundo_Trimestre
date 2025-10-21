from Ejer_36 import Televisor36

# --------------------
# Ejercicio 92
# Clase ControlRemoto que maneja un televisor (composición).
# --------------------
class ControlRemoto92:
    """Control remoto que ajusta el volumen de un Televisor36."""
    def __init__(self, televisor):
        self.tv = televisor

    def subir_volumen(self):
        return self.tv.ajustar_volumen(5)

# Prueba del ejercicio 92
tv92 = Televisor36()
cr92 = ControlRemoto92(tv92)
print("E92 subir vol:", cr92.subir_volumen())