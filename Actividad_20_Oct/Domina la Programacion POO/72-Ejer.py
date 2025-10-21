# --------------------
# Ejercicio 72
# Clase Restaurante con propinas acumuladas.
# --------------------
class Restaurante72:
    """Restaurante que acumula propinas."""
    def __init__(self):
        self.propinas = 0

    def agregar_propina(self, monto):
        self.propinas += monto
        return self.propinas

# Prueba del ejercicio 72
r72 = Restaurante72()
print("E72 propina total:", r72.agregar_propina(10000))