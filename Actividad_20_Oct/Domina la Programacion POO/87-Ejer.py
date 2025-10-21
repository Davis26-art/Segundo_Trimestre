# --------------------
# Ejercicio 87
# Clase NotaMusical con frecuencia y método reproducir (simulado).
# --------------------
class NotaMusical87:
    """Nota musical representada por frecuencia."""
    def __init__(self, frecuencia):
        self.frecuencia = frecuencia

    def reproducir(self):
        return f"Reproduciendo nota {self.frecuencia}Hz"

# Prueba del ejercicio 87
n87 = NotaMusical87(440)
print("E87:", n87.reproducir())