# --------------------
# Ejercicio 17
# Clase CalculadoraIMC para calcular índice de masa corporal.
# --------------------
class CalculadoraIMC17:
    """Calcula IMC: peso(kg) / altura(m)^2 y clasifica."""
    def __init__(self, peso, altura_m):
        self.peso = peso
        self.altura = altura_m

    def imc(self):
        if self.altura <= 0:
            return None
        return self.peso / (self.altura ** 2)

    def clasificar(self):
        val = self.imc()
        if val is None:
            return "altura inválida"
        if val < 18.5:
            return "bajo peso"
        if val < 25:
            return "normal"
        if val < 30:
            return "sobrepeso"
        return "obesidad"

# Prueba del ejercicio 17
calc_imc = CalculadoraIMC17(70, 1.75)
print("E17 imc:", round(calc_imc.imc(),2), "clasif:", calc_imc.clasificar())