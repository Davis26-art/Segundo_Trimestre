# --------------------
# Ejercicio 03
# Clase Calculadora con operaciones básicas (métodos puros).
# --------------------
class Calculadora03:
    """Calculadora con suma, resta, multiplicación y división (manejo básico de división por cero)."""
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        # si b es 0 devolvemos None para indicar error
        if b == 0:
            return None
        return a / b

# Prueba del ejercicio 03
calc = Calculadora03()
print("E03 5+3=", calc.sumar(5,3))
print("E03 10/0=", calc.dividir(10,0))  # None