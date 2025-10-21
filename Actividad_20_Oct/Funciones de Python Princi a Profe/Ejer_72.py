#---------------------------------------------------------------
# Ejercicio 72 — absoluto(n)
#---------------------------------------------------------------

def absoluto(n):
    # Retorna el valor absoluto de n
    return n if n >= 0 else -n

if __name__ == "__main__":
    print(absoluto(-10))  # 10
