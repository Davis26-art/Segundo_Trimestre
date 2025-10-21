# --------------------
# Ejercicio 25
# Clase Nota con contenido y etiqueta, y método para mostrar resumen.
# --------------------
class Nota25:
    """Nota simple con texto y etiqueta (tag)."""
    def __init__(self, contenido, etiqueta="general"):
        self.contenido = contenido
        self.etiqueta = etiqueta

    def resumen(self, largo=20):
        # devuelve un prefijo del contenido limitado a 'largo' caracteres
        return (self.contenido[:largo] + "...") if len(self.contenido) > largo else self.contenido

# Prueba del ejercicio 25
n = Nota25("Comprar leche, pan y huevos", "compras")
print("E25 resumen:", n.resumen(10))