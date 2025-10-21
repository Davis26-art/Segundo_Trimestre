from Ejer_11 import Mascota11

# --------------------
# Ejercicio 35
# Clase CuidadorMascotas que registra mascotas (lista de objetos Mascota11) y cuenta.
# --------------------
class Cuidador35:
    """Cuidador que administra una lista de mascotas y puede contar cuántas tiene."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.mascotas = []

    def registrar_mascota(self, mascota):
        if hasattr(mascota, "nombre"):
            self.mascotas.append(mascota)
            return True
        return False

    def contar(self):
        return len(self.mascotas)

# Prueba del ejercicio 35
cu = Cuidador35("Ana")
cu.registrar_mascota(Mascota11("Fido", "perro"))
print("E35 contar mascotas:", cu.contar())