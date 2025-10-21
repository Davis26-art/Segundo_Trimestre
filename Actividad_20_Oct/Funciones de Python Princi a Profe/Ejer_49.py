#---------------------------------------------------------------
# Ejercicio 49 — aplicar_descuento(precio, descuento_pct)
#---------------------------------------------------------------

def aplicar_descuento(precio, descuento_pct):
    # Resta porcentaje (ej: 10 significa 10%)
    return precio * (1 - descuento_pct / 100.0)

if __name__ == "__main__":
    print(aplicar_descuento(100, 10))  # 90.0
