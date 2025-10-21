# --------------------
# Ejercicio 32
# Clase Usuario con autenticación muy básica (compara contraseñas en memoria).
# --------------------
class Usuario32:
    """Usuario con nombre y contraseña simple (no segura, solo para ejercicio)."""
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self._contrasena = contrasena  # atributo 'privado' por convención

    def autenticar(self, intento):
        return intento == self._contrasena

# Prueba del ejercicio 32
u = Usuario32("david", "secreto")
print("E32 autenticar 'no' ->", u.autenticar("no"), "autenticar 'secreto' ->", u.autenticar("secreto"))