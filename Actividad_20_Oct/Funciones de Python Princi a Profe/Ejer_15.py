#---------------------------------------------------------------
# Ejercicio 15 — es_primo(n)
#---------------------------------------------------------------

def es_primo(n):
    # Determina si n es primo (n >= 2)
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == "__main__":
    print("es_primo(13) ->", es_primo(13))  # True
    print("es_primo(12) ->", es_primo(12))  # False
