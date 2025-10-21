# --------------------
# Ejercicio 33
# Clase SerieTV con episodios (lista) y método para ver siguiente episodio.
# --------------------
class Serie33:
    """Serie con lista de títulos de episodios y puntero al episodio actual."""
    def __init__(self, titulo, episodios):
        self.titulo = titulo
        self.episodios = episodios[:]
        self.indice_actual = 0

    def siguiente(self):
        if self.indice_actual < len(self.episodios):
            ep = self.episodios[self.indice_actual]
            self.indice_actual += 1
            return ep
        return None

# Prueba del ejercicio 33
s = Serie33("Mi Serie", ["E1","E2","E3"])
print("E33 siguiente:", s.siguiente(), s.siguiente(), s.siguiente(), s.siguiente())