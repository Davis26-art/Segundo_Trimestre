# --------------------
# Ejercicio 01
# Clase simple Persona con nombre y edad, y métodos básicos.
# --------------------
class Persona01:
    """Clase Persona sencilla: almacena nombre y edad, puede saludar y envejecer."""
    def __init__(self, nombre, edad):
        # guarda el nombre y la edad en la instancia
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        # devuelve un saludo con el nombre de la persona
        return f"Hola, soy {self.nombre}."

    def cumplir_anios(self):
        # incrementa la edad en 1 y devuelve la nueva edad
        self.edad += 1
        return self.edad

# Prueba del ejercicio 01
p1 = Persona01("Ana", 30)
print("E01 saludar:", p1.saludar())             # Esperado: "Hola, soy Ana."
print("E01 edad antes:", 30, "después:", p1.cumplir_anios())  # 31