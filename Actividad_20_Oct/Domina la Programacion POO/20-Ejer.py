# --------------------
# Ejercicio 20
# Clase TarjetaRegalo con balance que se descuenta en compras.
# --------------------
class Tarjeta20:
    """Tarjeta regalo con balance; permite gastar y recargar."""
    def __init__(self, saldo=0):
        self.saldo = float(saldo)

    def gastar(self, cantidad):
        if cantidad <= 0 or cantidad > self.saldo:
            return False
        self.saldo -= cantidad
        return True

    def recargar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False

# Prueba del ejercicio 20
tg = Tarjeta20(50)
print("E20 gastar 20 ->", tg.gastar(20), "saldo:", tg.saldo)
print("E20 recargar 30 ->", tg.recargar(30), "saldo:", tg.saldo)