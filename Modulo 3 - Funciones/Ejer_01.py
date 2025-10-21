# =========================================
# FUNCIÓN PARA CALCULAR ÁREA DE UN RECTÁNGULO
# =========================================

def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

# Bloque de prueba
mi_base = 5
mi_altura = 3
area_calculada = calcular_area_rectangulo(mi_base, mi_altura)
print(f"El área del rectángulo es: {area_calculada}")
