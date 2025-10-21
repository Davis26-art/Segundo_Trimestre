from Ejer_37 import Orden37, Producto04

# --------------------
# Ejercicio 42
# Clase PedidoConEnvio que extiende Orden37 y añade costo de envío fijo.
# --------------------
class Pedido42(Orden37):
    """Pedido con cálculo de total que incluye costo de envío."""
    def __init__(self, costo_envio=5.0):
        super().__init__()
        self.costo_envio = float(costo_envio)

    def total_con_envio(self):
        return self.total() + self.costo_envio

# Prueba del ejercicio 42
p42 = Pedido42(3.5)
p42.agregar_item(Producto04("Lapiz", 0.5, 100), 2)
print("E42 total con envio:", p42.total_con_envio())