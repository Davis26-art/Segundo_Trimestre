# --------------------
# Ejercicio 73
# Clase Bateria con porcentaje y método descargar/cargar.
# --------------------
class Bateria73:
    """Batería que puede descargarse o cargarse en porcentaje."""
    def __init__(self, nivel=100):
        self.nivel = nivel

    def descargar(self, pct):
        self.nivel = max(0, self.nivel - pct)
        return self.nivel

    def cargar(self, pct):
        self.nivel = min(100, self.nivel + pct)
        return self.nivel

# Prueba del ejercicio 73
bat = Bateria73()
print("E73 descargar 30:", bat.descargar(30), "cargar 10:", bat.cargar(10))