# --------------------
# Ejercicio 15
# Clase Temperatura con conversión entre C y F.
# --------------------
class Temperatura15:
    """Temperatura con métodos de conversión Celsius <-> Fahrenheit."""
    def __init__(self, celsius):
        self.celsius = float(celsius)

    def a_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def set_celsius(self, c):
        self.celsius = float(c)

# Prueba del ejercicio 15
temp = Temperatura15(0)
print("E15 0C -> F:", temp.a_fahrenheit())