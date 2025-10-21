from Ejer_04 import Producto04

# --------------------
# Ejercicio 27
# Clase ProductoConDescuento hereda de Producto04 y añade método aplicar_descuento.
# --------------------
class Producto27(Producto04):
    """Producto con capacidad de aplicar porcentaje de descuento al precio."""
    def aplicar_descuento(self, pct):
        # pct en decimal: 0.1 -> 10%
        if not (0 <= pct <= 1):
            return False
        self.precio = self.precio * (1 - pct)
        return True

# Prueba del ejercicio 27
p27 = Producto27("Cuaderno", 10, 50)
print("E27 precio antes:", p27.precio)
p27.aplicar_descuento(0.2)
print("E27 precio después 20%:", p27.precio)