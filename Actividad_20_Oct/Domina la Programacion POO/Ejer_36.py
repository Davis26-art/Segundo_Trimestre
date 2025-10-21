# --------------------
# Ejercicio 36
# Clase Televisor con volumen y canal; métodos cambiar canal y ajustar volumen.
# --------------------
class Televisor36:
    """Televisor con control de canal y volumen (volumen 0..100)."""
    def __init__(self):
        self.canal = 1
        self.volumen = 20

    def cambiar_canal(self, canal):
        if canal >= 1:
            self.canal = int(canal)
        return self.canal

    def ajustar_volumen(self, delta):
        self.volumen = max(0, min(100, self.volumen + int(delta)))
        return self.volumen

# Prueba del ejercicio 36
tv = Televisor36()
print("E36 cambiar canal 5:", tv.cambiar_canal(5), "vol +10:", tv.ajustar_volumen(10))