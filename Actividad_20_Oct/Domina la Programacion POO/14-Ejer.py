# --------------------
# Ejercicio 14
# Clase Contador que incrementa, decrementa y puede devolver el valor.
# --------------------
class Contador14:
    """Contador simple con métodos incrementar y decrementar."""
    def __init__(self, inicio=0):
        self.valor = inicio

    def incrementar(self):
        self.valor += 1
        return self.valor

    def decrementar(self):
        self.valor -= 1
        return self.valor

# Prueba del ejercicio 14
c = Contador14(5)
print("E14 inc:", c.incrementar(), "dec:", c.decrementar())