from Ejer_04 import Producto04

# --------------------
# Ejercicio 37
# Clase OrdenPedido con items y método calcular_total (usando objeto Producto04).
# --------------------
class Orden37:
    """Orden que contiene (producto, cantidad) y calcula total."""
    def __init__(self):
        self.items = []  # lista de tuplas (producto, cantidad)

    def agregar_item(self, producto, cantidad):
        if cantidad > 0:
            self.items.append((producto, int(cantidad)))
            return True
        return False

    def total(self):
        return sum(prod.precio * cant for prod, cant in self.items)

# Prueba del ejercicio 37
o = Orden37()
o.agregar_item(Producto04("Lapiz", 0.5, 100), 10)
o.agregar_item(Producto04("Cuaderno", 2, 50), 2)
print("E37 total orden:", o.total())