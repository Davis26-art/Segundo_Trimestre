from Ejer_61 import Carta61

# --------------------
# Ejercicio 62
# Clase Baraja que genera un conjunto de cartas.
# --------------------
class Baraja62:
    """Baraja de 52 cartas (simplificada)."""
    def __init__(self):
        valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
        self.cartas = [Carta61(v, p) for v in valores for p in palos]

    def sacar_carta(self):
        return self.cartas.pop() if self.cartas else None

# Prueba del ejercicio 62
b = Baraja62()
print("E62 sacar carta:", b.sacar_carta().mostrar())
