#---------------------------------------------
# Ejercicio 5 — Clase Producto de Tienda
#---------------------------------------------


class Producto:
    def __init__(self, nombre, precio, stock): #Convierte precio y stock a tipos numéricos seguros.
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = int(stock)

    def mostrar_info(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock} unidades."

    def actualizar_stock(self, cantidad): # actualizar_stock puede usarse para reposición (+) o venta (-).
        # cantidad positiva->añade, negativa->quita (venta)
        self.stock += cantidad
        return f"Stock actualizado. Nuevo stock de {self.nombre}: {self.stock} unidades."

    def calcular_valor_total(self, unidades):
        if unidades <= 0:
            return "La cantidad de unidades debe ser positiva."
        if unidades > self.stock:
            return f"Stock insuficiente para {unidades} unidades de {self.nombre}."
        return f"El valor total de {unidades} unidades de {self.nombre} es ${unidades * self.precio:.2f}."

if __name__ == "__main__":
    laptop = Producto("Laptop Gaming", 1200.00, 10)
    print(laptop.mostrar_info())
    print(laptop.actualizar_stock(5))
    print(laptop.mostrar_info())
    print(laptop.calcular_valor_total(3))
    print(laptop.calcular_valor_total(18))
    print(laptop.actualizar_stock(-2))
    print(laptop.mostrar_info())
    print(laptop.calcular_valor_total(10))


