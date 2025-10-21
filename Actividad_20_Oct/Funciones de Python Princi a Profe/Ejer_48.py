#---------------------------------------------------------------
# Ejercicio 48 — porcentaje_de(parte, total)
#---------------------------------------------------------------

def porcentaje_de(parte, total):
    # Calcula qué porcentaje representa 'parte' de 'total'
    if total == 0:
        return None
    return (parte / total) * 100

if __name__ == "__main__":
    print(porcentaje_de(25, 200))  # 12.5
