#---------------------------------------------------------------
# Ejercicio 50 — agregar_impuesto(precio, impuesto_pct)
#---------------------------------------------------------------

def agregar_impuesto(precio, impuesto_pct):
    # Añade impuesto porcentual
    return precio * (1 + impuesto_pct / 100.0)

if __name__ == "__main__":
    print(agregar_impuesto(100, 19))  # 119.0
