# --------------------
# Ejercicio 75
# Clase TemporizadorCuentaRegresiva con segundos iniciales.
# --------------------
class Temporizador75:
    """Cuenta regresiva simple (disminuye segundos)."""
    def __init__(self, segundos):
        self.segundos = segundos

    def tic(self):
        if self.segundos > 0:
            self.segundos -= 1
        return self.segundos

# Prueba del ejercicio 75
tmp = Temporizador75(5)
for _ in range(3):
    print("E75 tic:", tmp.tic())