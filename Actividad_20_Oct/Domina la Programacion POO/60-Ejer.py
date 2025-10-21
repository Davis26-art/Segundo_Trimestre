# --------------------
# Ejercicio 60
# Clase RelojAlarma que puede establecer y verificar hora de alarma.
# --------------------
class RelojAlarma60:
    """Reloj con alarma configurable (horas:minutos)."""
    def __init__(self):
        self.hora_alarma = None

    def configurar_alarma(self, hora, minuto):
        self.hora_alarma = (hora, minuto)

    def sonar(self, hora_actual, minuto_actual):
        return self.hora_alarma == (hora_actual, minuto_actual)

# Prueba del ejercicio 60
ra = RelojAlarma60()
ra.configurar_alarma(7, 30)
print("E60 sonar 7:30?", ra.sonar(7, 30))