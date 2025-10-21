import random

# --------------------
# Ejercicio 18
# Clase JuegoAdivinaNúmero (usa random) con método intentar.
# --------------------
class JuegoAdivina18:
    """Juego simple: adivinar un número entre 1 y max_n. Mantiene estado de intentos."""
    def __init__(self, max_n=10):
        self.max_n = max_n
        self.objetivo = random.randint(1, max_n)
        self.intentos = 0

    def intentar(self, n):
        self.intentos += 1
        if n == self.objetivo:
            return "acertó"
        if n < self.objetivo:
            return "mayor"
        return "menor"

# Prueba del ejercicio 18
j = JuegoAdivina18(5)
print("E18 objetivo (oculto):", j.objetivo)
print("E18 intento 1:", j.intentar(1))