from Ejer_02 import Cuenta02

# --------------------
# Ejercicio 29
# Clase Banco que administra múltiples cuentas (dict titular->Cuenta02)
# --------------------
class Banco29:
    """Banco muy simple que guarda cuentas por titular (sustituyendo si existe)."""
    def __init__(self):
        self.cuentas = {}

    def abrir_cuenta(self, titular, saldo_inicial=0):
        self.cuentas[titular] = Cuenta02(titular, saldo_inicial)
        return self.cuentas[titular]

    def saldo_titular(self, titular):
        acc = self.cuentas.get(titular)
        return acc.consultar_saldo() if acc else None

# Prueba del ejercicio 29
b = Banco29()
b.abrir_cuenta("Ana", 500)
print("E29 saldo Ana:", b.saldo_titular("Ana"))
