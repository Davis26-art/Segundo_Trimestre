# --------------------
# Ejercicio 61
# Clase Carta con valor y palo.
# --------------------
class Carta61:
    """Carta de baraja con valor y palo."""
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def mostrar(self):
        return f"{self.valor} de {self.palo}"

# Prueba del ejercicio 61
carta = Carta61("As", "Corazones")
print("E61:", carta.mostrar())