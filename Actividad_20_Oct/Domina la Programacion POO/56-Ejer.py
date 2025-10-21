# --------------------
# Ejercicio 56
# Clase Cajero con dinero total y métodos para retirar y depositar.
# --------------------
class Cajero56:
    """Cajero con un monto de dinero total y operaciones básicas."""
    def __init__(self, dinero_total):
        self.dinero_total = dinero_total

    def retirar(self, monto):
        if 0 < monto <= self.dinero_total:
            self.dinero_total -= monto
            return True
        return False

    def depositar(self, monto):
        if monto > 0:
            self.dinero_total += monto
            return True
        return False

# Prueba del ejercicio 56
cj = Cajero56(1000)
print("E56 retirar 200 ->", cj.retirar(200), "total:", cj.dinero_total)
print("E56 depositar 100 ->", cj.depositar(100), "total:", cj.dinero_total)