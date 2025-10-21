# --------------------
# Ejercicio 13
# Clase AgendaSimple que guarda contactos en dict y permite añadir y obtener.
# --------------------
class Agenda13:
    """Agenda simple usando diccionario: nombre -> teléfono."""
    def __init__(self):
        self.contactos = {}

    def agregar(self, nombre, telefono):
        self.contactos[nombre] = telefono
        return True

    def obtener(self, nombre):
        return self.contactos.get(nombre)

# Prueba del ejercicio 13
ag = Agenda13()
ag.agregar("Marta", "3001234567")
print("E13 obtener Marta:", ag.obtener("Marta"))














