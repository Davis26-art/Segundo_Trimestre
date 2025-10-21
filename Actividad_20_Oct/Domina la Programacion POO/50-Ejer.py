# --------------------
# Ejercicio 50
# Clase Conversacion con mensajes (lista) y método enviar (agrega mensaje con emisor).
# --------------------
class Conversacion50:
    """Conversación simple que contiene tuplas (emisor, texto)."""
    def __init__(self):
        self.mensajes = []

    def enviar(self, emisor, texto):
        self.mensajes.append((emisor, texto))
        return True

    def ultimos(self, n=5):
        return self.mensajes[-n:]

# Prueba del ejercicio 50
conv = Conversacion50()
conv.enviar("Ana", "Hola")
conv.enviar("Juan", "Hola Ana")
print("E50 ultimos mensajes:", conv.ultimos(2))