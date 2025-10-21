# --------------------
# Ejercicio 44
# Clase Reloj que almacena hora (h,m) y permite avanzar minutos.
# --------------------
class Reloj44:
    """Reloj sencillo que maneja horas y minutos en formato 24h (sin validación exhaustiva)."""
    def __init__(self, h=0, m=0):
        self.h = int(h) % 24
        self.m = int(m) % 60

    def avanzar_minutos(self, minutos):
        total = self.h * 60 + self.m + int(minutos)
        self.h = (total // 60) % 24
        self.m = total % 60
        return (self.h, self.m)

# Prueba del ejercicio 44
r = Reloj44(23,50)
print("E44 avanzar 20m ->", r.avanzar_minutos(20))