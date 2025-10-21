import random

# --------------------
# Ejercicio 99
# Clase TemporizadorAleatorio que cuenta segundos al azar.
# --------------------
class TemporizadorAleatorio99:
    """Temporizador que genera tiempos aleatorios para eventos."""
    def generar(self):
        return random.randint(1, 60)

# Prueba del ejercicio 99
ta = TemporizadorAleatorio99()
print("E99 tiempo aleatorio:", ta.generar())