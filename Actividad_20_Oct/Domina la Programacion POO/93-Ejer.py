# --------------------
# Ejercicio 93
# Clase RegistroLlamadas con lista de llamadas.
# --------------------
class RegistroLlamadas93:
    """Registro simple de llamadas telefónicas."""
    def __init__(self):
        self.llamadas = []

    def registrar(self, numero, duracion):
        self.llamadas.append((numero, duracion))
        return True

    def total_duracion(self):
        return sum(d for _, d in self.llamadas)

# Prueba del ejercicio 93
rl = RegistroLlamadas93()
rl.registrar("3001112222", 5)
print("E93 total minutos:", rl.total_duracion())