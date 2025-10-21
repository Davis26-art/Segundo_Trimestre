# --------------------
# Ejercicio 70
# Clase Correo con remitente, destinatario y mensaje.
# --------------------
class Correo70:
    """Correo electrónico con remitente, destinatario y mensaje."""
    def __init__(self, de_, para, mensaje):
        self.de_ = de_
        self.para = para
        self.mensaje = mensaje

    def mostrar(self):
        return f"De: {self.de_} | Para: {self.para} | {self.mensaje}"

# Prueba del ejercicio 70
c70 = Correo70("ana@mail.com", "juan@mail.com", "Hola Juan")
print("E70:", c70.mostrar())