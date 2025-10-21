#---------------------------------------------------------------
# Ejercicio 45 — parse_int_seguro(s, default=0)
#---------------------------------------------------------------

def parse_int_seguro(s, default=0):
    # Intenta convertir a int; si falla devuelve default
    try:
        return int(s)
    except (ValueError, TypeError):
        return default

if __name__ == "__main__":
    print(parse_int_seguro("123"))  # 123
    print(parse_int_seguro("abc", -1))  # -1
