# --------------------
# Ejercicio 47
# Clase CuentaMonedero con método transferir a otra cuenta (si suficiente saldo).
# --------------------
class CuentaMonedero47:
    """Monedero simple que permite transferir saldo a otro monedero."""
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = float(saldo)

    def transferir(self, destino, cantidad):
        if cantidad <= 0 or cantidad > self.saldo:
            return False
        self.saldo -= cantidad
        destino.saldo += cantidad
        return True

# Prueba del ejercicio 47
m1 = CuentaMonedero47("A", 100)
m2 = CuentaMonedero47("B", 10)
print("E47 transferir 30 ->", m1.transferir(m2, 30), "m1:", m1.saldo, "m2:", m2.saldo)