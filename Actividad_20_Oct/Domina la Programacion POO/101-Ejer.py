#---------------------------------------------
# Ejercicio 1 — Clase Persona Básica
#---------------------------------------------


class Persona: # define la clase
    def __init__(self, nombre, edad): #constructor que recibe nombre y edad.
        # inicializa atributos de instancia
        self.nombre = nombre #guardan atributos en la instancia.
        self.edad = edad #guardan atributos en la instancia.

    def saludar(self):  #devuelve un saludo formateado.
        return f"Hola, mi nombre es {self.nombre}."

    def cumplir_anios(self): #incrementa self.edad y devuelve mensaje.
        self.edad += 1
        return f"¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años."

if __name__ == "__main__": #creamos instancias y probamos métodos.
    persona1 = Persona("Ana", 30)
    print(persona1.saludar())
    print(persona1.cumplir_anios())
    print(persona1.saludar())

    persona2 = Persona("Carlos", 25)
    print(persona2.saludar())


