# --------------------
# Ejercicio 91
# Clase CajaRegistradora que acumula ventas y calcula IVA.
# --------------------
class CajaRegistradora91:
    """Caja que acumula ventas y calcula total con IVA."""
    def __init__(self, iva=0.19):
        self.ventas = []
        self.iva = iva

    def registrar_venta(self, valor):
        self.ventas.append(valor)
        return True

    def total_con_iva(self):
        bruto = sum(self.ventas)
        return bruto * (1 + self.iva)

# Prueba del ejercicio 91
cr = CajaRegistradora91()
cr.registrar_venta(10000)
print("E91 total con IVA:", cr.total_con_iva())