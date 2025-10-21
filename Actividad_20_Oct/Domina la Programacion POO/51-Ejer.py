
import random

# --------------------
# Ejercicio 51
# Clase Dado con método lanzar que devuelve número aleatorio entre 1 y 6.
# --------------------
class Dado51:
    """Dado que al lanzarse devuelve un número entre 1 y 6."""
    def lanzar(self):
        return random.randint(1, 6)

# Prueba del ejercicio 51
d = Dado51()
print("E51 lanzar dado:", d.lanzar())
