# --------------------
# Ejercicio 23
# Clase CuentaAhorro con interés simple calculable.
# --------------------
class CuentaAhorro23:
    """Cuenta ahorro con método para aplicar interés simple anual."""
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = float(saldo)

    def aplicar_interes_simple(self, tasa, años=1):
        # tasa en decimal, ejemplo 0.05 -> 5%
        if tasa < 0 or años < 0:
            return None
        return self.saldo * (1 + tasa * años)

# Prueba del ejercicio 23
ca = CuentaAhorro23("Sofia", 1000)
print("E23 saldo con 5% por 1 año:", ca.aplicar_interes_simple(0.05, 1))