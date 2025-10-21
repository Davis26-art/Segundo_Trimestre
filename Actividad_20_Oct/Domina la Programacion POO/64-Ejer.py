# --------------------
# Ejercicio 64
# Clase CarritoCompra que suma precios de productos.
# --------------------
class Carrito64:
    """Carrito de compras con productos y cálculo de total."""
    def __init__(self):
        self.productos = []

    def agregar(self, producto, precio):
        self.productos.append((producto, precio))
        return True

    def total(self):
        return sum(p[1] for p in self.productos)

# Prueba del ejercicio 64
car = Carrito64()
car.agregar("Lapicero", 2000)
car.agregar("Borrador", 500)
print("E64 total compra:", car.total())