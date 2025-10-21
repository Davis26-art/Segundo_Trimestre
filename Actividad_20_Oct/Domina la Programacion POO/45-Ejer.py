# --------------------
# Ejercicio 45
# Clase CuentaUsuario con bloqueo tras N intentos fallidos (estado).
# --------------------
class CuentaUsuario45:
    """Cuenta de usuario con control simple de intentos y bloqueo."""
    def __init__(self, nombre, contrasena, max_intentos=3):
        self.nombre = nombre
        self._contrasena = contrasena
        self.max_intentos = max_intentos
        self.intentos = 0
        self.bloqueada = False

    def intentar_login(self, intento):
        if self.bloqueada:
            return "bloqueada"
        if intento == self._contrasena:
            self.intentos = 0
            return "acceso"
        self.intentos += 1
        if self.intentos >= self.max_intentos:
            self.bloqueada = True
            return "bloqueada"
        return f"fallo {self.intentos}"

# Prueba del ejercicio 45
cu45 = CuentaUsuario45("user", "1234", 2)
print("E45 intento1:", cu45.intentar_login("0000"))
print("E45 intento2:", cu45.intentar_login("0000"))
print("E45 intento3:", cu45.intentar_login("1234"))