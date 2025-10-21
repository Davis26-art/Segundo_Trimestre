# --------------------
# Ejercicio 59
# Clase Tienda que guarda ventas totales.
# --------------------
class Tienda59:
    """Tienda con contador de ventas acumuladas."""
    def __init__(self, nombre):
        self.nombre = nombre
        self.ventas = 0

    def registrar_venta(self, monto):
        if monto > 0:
            self.ventas += monto
            return True
        return False

# Prueba del ejercicio 59
t = Tienda59("Papelería ABC")
t.registrar_venta(15000)
print("E59 total ventas:", t.ventas)