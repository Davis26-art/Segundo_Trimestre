#---------------------------------------------
# Ejercicio 3 — Clase CuentaBancaria
#---------------------------------------------


class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, cantidad): #validan entrada, mantienen self.saldo consistente
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}"
        return "La cantidad a depositar debe ser positiva."

    def retirar(self, cantidad): #validan entrada, mantienen self.saldo consistente
        if cantidad <= 0:
            return "La cantidad a retirar debe ser positiva."
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            return f"Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}"
        return "Saldo insuficiente."

    def consultar_saldo(self):
        return f"Saldo actual: {self.saldo}"

if __name__ == "__main__":
    cuenta = CuentaBancaria(1000)
    print(cuenta.consultar_saldo())
    print(cuenta.depositar(500))
    print(cuenta.retirar(200))
    print(cuenta.retirar(1500))  # saldo insuficiente
    print(cuenta.consultar_saldo())
    print(cuenta.depositar(-100))  # cantidad inválida


