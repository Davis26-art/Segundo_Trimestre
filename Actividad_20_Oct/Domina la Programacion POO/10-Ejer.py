# --------------------
# Ejercicio 10
# Clase Temporizador simple que almacena tiempo y permite resetear.
# --------------------
class Temporizador10:
    """Temporizador simple: no usa tiempo real, solo almacena un valor numérico."""
    def __init__(self):
        self.tiempo = 0  # en unidades arbitrarias

    def avanzar(self, delta):
        if delta > 0:
            self.tiempo += delta
        return self.tiempo

    def reset(self):
        self.tiempo = 0
        return self.tiempo

# Prueba del ejercicio 10
t = Temporizador10()
print("E10 avanzar 5 ->", t.avanzar(5))
print("E10 reset ->", t.reset())