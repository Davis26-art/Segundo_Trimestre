# --------------------
# Ejercicio 04
# Clase Producto con nombre, precio y stock; métodos para actualizar stock y calcular valor.
# --------------------
class Producto04:
    """Producto con información básica y operaciones de inventario."""
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = int(stock)

    def actualizar_stock(self, delta):
        # delta positivo: entrada; negativo: salida/venta
        self.stock += int(delta)
        return self.stock

    def valor_total(self):
        # valor total del inventario del producto
        return self.precio * self.stock

# Prueba del ejercicio 04
prod = Producto04("Lapiz", 0.5, 100)
print("E04 stock inicial:", prod.stock)
print("E04 actualizar -10 ->", prod.actualizar_stock(-10), "valor total:", prod.valor_total())