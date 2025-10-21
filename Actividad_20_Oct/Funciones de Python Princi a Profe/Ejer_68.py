#---------------------------------------------------------------
# Ejercicio 68 — convertir_a_hexadecimal(n)
#---------------------------------------------------------------

def convertir_a_hexadecimal(n):
    # Retorna representación hexadecimal sin prefijo '0x'
    return hex(n)[2:]

if __name__ == "__main__":
    print(convertir_a_hexadecimal(255))  # 'ff'
