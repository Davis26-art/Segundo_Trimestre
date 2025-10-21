from Ejer_04 import Producto04

# --------------------
# Ejercicio 30
# Clase Inventario que gestiona múltiples productos (nombre->Producto04)
# --------------------
class Inventario30:
    """Inventario básico: guardar productos por nombre."""
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        # producto debe tener atributo nombre
        self.productos[producto.nombre] = producto
        return True

    def total_valor(self):
        # suma valor_total de cada producto
        return sum(p.valor_total() for p in self.productos.values())

# Prueba del ejercicio 30
inv = Inventario30()
inv.agregar_producto(Producto04("Lapiz", 0.5, 100))
inv.agregar_producto(Producto04("Cuaderno", 2, 50))
print("E30 total valor inventario:", inv.total_valor())