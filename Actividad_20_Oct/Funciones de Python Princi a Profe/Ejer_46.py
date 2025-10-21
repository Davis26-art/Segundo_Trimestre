#---------------------------------------------------------------
# Ejercicio 46 — parse_float_seguro(s, default=0.0)
#---------------------------------------------------------------

def parse_float_seguro(s, default=0.0):
    # Intenta convertir a float; si falla devuelve default
    try:
        return float(s)
    except (ValueError, TypeError):
        return default

if __name__ == "__main__":
    print(parse_float_seguro("3.14"))  # 3.14
    print(parse_float_seguro("nope", -1.0))  # -1.0
