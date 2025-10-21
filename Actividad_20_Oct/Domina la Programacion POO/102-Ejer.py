#---------------------------------------------
# Ejercicio 2 — Clase Calculadora
#---------------------------------------------


class Calculadora:
    def __init__(self):
        pass  # no necesita estado

    def sumar(self, num1, num2):
        return num1 + num2

    def restar(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2): #incorpora validación para evitar división por cero.
        if num2 != 0:
            return num1 / num2
        return "Error: División por cero no permitida."

if __name__ == "__main__": #Métodos realizan operaciones
    calc = Calculadora()
    print("5 + 3 =", calc.sumar(5, 3))
    print("10 - 4 =", calc.restar(10, 4))
    print("6 * 7 =", calc.multiplicar(6, 7))
    print("20 / 5 =", calc.dividir(20, 5))
    print("10 / 0 =", calc.dividir(10, 0))


