# --------------------
# Ejercicio 63
# Clase Restaurante con menú y método para agregar platos.
# --------------------
class Restaurante63:
    """Restaurante con menú (diccionario nombre->precio)."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.menu = {}

    def agregar_plato(self, plato, precio):
        self.menu[plato] = precio
        return True

    def mostrar_menu(self):
        return self.menu

# Prueba del ejercicio 63
r63 = Restaurante63("La Buena Mesa")
r63.agregar_plato("Pasta", 12000)
print("E63 menú:", r63.mostrar_menu())