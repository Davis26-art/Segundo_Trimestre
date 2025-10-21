import random

# --------------------
# Ejercicio 85
# Clase JuegoDados que lanza dos dados.
# --------------------
class JuegoDados85:
    """Lanza dos dados y suma el resultado."""
    def jugar(self):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        return d1, d2, d1+d2

# Prueba del ejercicio 85
jd = JuegoDados85()
print("E85 jugar:", jd.jugar())