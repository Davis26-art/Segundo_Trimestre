#---------------------------------------------
# Ejercicio 6 — Clase Estudiante con Calificaciones
#---------------------------------------------


class Estudiante:
    def __init__(self, nombre, id_estudiante):
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.calificaciones = []

    def agregar_calificacion(self, nota): #es una lista que guarda notas.
        if 0 <= nota <= 5:  # supongamos escala 0-5
            self.calificaciones.append(nota)
            return f"Nota {nota} agregada."
        return "Nota inválida. Debe estar entre 0 y 5."

    def promedio(self): #maneja el caso sin calificaciones devolviendo 0.0.
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)

    def mostrar_datos(self):
        return f"{self.nombre} (ID: {self.id_estudiante}) - Promedio: {self.promedio():.2f}"

if __name__ == "__main__":
    est = Estudiante("María", "E001")
    print(est.agregar_calificacion(4.5))
    print(est.agregar_calificacion(5))
    print(est.agregar_calificacion(3.7))
    print(est.mostrar_datos())
    print("Calificaciones:", est.calificaciones)

