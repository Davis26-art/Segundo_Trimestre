# --------------------
# Ejercicio 24
# Clase Contacto con validación simple de email (método).
# --------------------
class Contacto24:
    """Contacto con nombre y email; método validar email muy básico."""
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def email_valido(self):
        # validación muy simple: contiene '@' y al menos un '.' en dominio
        if "@" not in self.email:
            return False
        user, domain = self.email.split("@", 1)
        return "." in domain and user != "" and domain.split(".")[0] != ""

# Prueba del ejercicio 24
ct = Contacto24("Pedro", "pedro@example.com")
print("E24 email valido:", ct.email_valido())