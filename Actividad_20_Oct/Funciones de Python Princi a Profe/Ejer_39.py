#---------------------------------------------------------------
# Ejercicio 39 — acronimo(frase)
#---------------------------------------------------------------

def acronimo(frase):
    # Toma las iniciales en mayúscula para formar acrónimo
    palabras = frase.split()
    return ''.join(p[0].upper() for p in palabras if p)

if __name__ == "__main__":
    print(acronimo("Organización de las Naciones Unidas"))  # 'ONU'
