# --------------------
# Ejercicio 48
# Clase ConversorMoneda con tasa fija y método convertir.
# --------------------
class Conversor48:
    """Conversor de moneda usando tasa fija (no fetch real)."""
    def __init__(self, tasa):
        self.tasa = float(tasa)  # cantidad de moneda destino por 1 moneda origen

    def convertir(self, monto):
        return monto * self.tasa

# Prueba del ejercicio 48
conv = Conversor48(0.00027)  # ejemplo COP -> USD aproximado
print("E48 10000 COP -> USD:", conv.convertir(10000))