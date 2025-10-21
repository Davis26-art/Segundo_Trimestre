# --------------------
# Ejercicio 78
# Clase ContadorClicks con incremento.
# --------------------
class ContadorClicks78:
    """Contador de clics acumulativos."""
    def __init__(self):
        self.contador = 0

    def click(self):
        self.contador += 1
        return self.contador

# Prueba del ejercicio 78
cc = ContadorClicks78()
for _ in range(3):
    cc.click()
print("E78 clics:", cc.contador)