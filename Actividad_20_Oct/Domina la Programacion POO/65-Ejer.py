# --------------------
# Ejercicio 65
# Clase Termometro con método subir y bajar temperatura.
# --------------------
class Termometro65:
    """Termómetro que ajusta temperatura en grados Celsius."""
    def __init__(self, temp_inicial=20):
        self.temperatura = temp_inicial

    def subir(self, grados):
        self.temperatura += grados
        return self.temperatura

    def bajar(self, grados):
        self.temperatura -= grados
        return self.temperatura

# Prueba del ejercicio 65
ter = Termometro65()
print("E65 subir 3:", ter.subir(3), "bajar 2:", ter.bajar(2))