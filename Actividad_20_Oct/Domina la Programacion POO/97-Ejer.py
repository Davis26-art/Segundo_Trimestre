# --------------------
# Ejercicio 97
# Clase Lavadora con métodos lavar y centrifugar.
# --------------------
class Lavadora97:
    """Lavadora con dos acciones principales."""
    def lavar(self):
        return "Lavando ropa..."

    def centrifugar(self):
        return "Centrifugando..."

# Prueba del ejercicio 97
lv = Lavadora97()
print("E97:", lv.lavar(), lv.centrifugar())