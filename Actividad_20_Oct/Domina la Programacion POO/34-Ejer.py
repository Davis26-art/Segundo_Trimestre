# --------------------
# Ejercicio 34
# Clase CalculadoraEstadistica con métodos mean y median (listas simples).
# --------------------
class CalculadoraEstadistica34:
    """Calculadora estadística muy simple: media y mediana (sin numpy)."""
    def mean(self, nums):
        return sum(nums)/len(nums) if nums else None

    def median(self, nums):
        if not nums:
            return None
        s = sorted(nums)
        n = len(s)
        mid = n // 2
        if n % 2 == 1:
            return s[mid]
        return (s[mid-1] + s[mid]) / 2

# Prueba del ejercicio 34
ce = CalculadoraEstadistica34()
print("E34 mean:", ce.mean([1,2,3]), "median [1,2,3,4]:", ce.median([1,2,3,4]))