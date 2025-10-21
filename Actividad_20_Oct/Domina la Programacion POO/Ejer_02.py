# --------------------
# Ejercicio 02
# Clase CuentaBancaria simple con depositar, retirar y consultar saldo.
# --------------------
class Cuenta02:
    """Cuenta bancaria básica: saldo inicial, depositar, retirar y consultar."""
    def __init__(self, titular, saldo_inicial=0):
        # titular: dueño de la cuenta; saldo_inicial: valor por defecto 0
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        # solo acepta cantidades positivas
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        # valida fondos y cantidad positiva
        if cantidad <= 0:
            return False
        if cantidad > self.saldo:
            return False
        self.saldo -= cantidad
        return True

    def consultar_saldo(self):
        # devuelve el saldo actual
        return self.saldo

# Prueba del ejercicio 02
c2 = Cuenta02("Carlos", 1000)
print("E02 saldo inicial:", c2.consultar_saldo())
print("E02 depositar 500 ->", c2.depositar(500), "saldo:", c2.consultar_saldo())
print("E02 retirar 2000 ->", c2.retirar(2000), "saldo:", c2.consultar_saldo())