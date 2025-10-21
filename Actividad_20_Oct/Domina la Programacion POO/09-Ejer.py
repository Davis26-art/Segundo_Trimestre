# --------------------
# Ejercicio 09
# Clase Rectangulo con area y perimetro.
# --------------------
class Rectangulo09:
    """Rectángulo: calculos de área y perímetro con base y altura."""
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

# Prueba del ejercicio 09
r = Rectangulo09(3, 4)
print("E09 area:", r.area(), "perimetro:", r.perimetro())