class Producto:
    def __init__(self, nombre, precio, stock):
        # Inicializa un objeto Producto con nombre, precio y stock.
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        # Actualiza el stock del producto sumando la cantidad especificada.
        self.stock += cantidad

    def __str__(self):
        # Retorna una representación en cadena del producto.
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.stock}"


class Cliente:
    def __init__(self, nombre, email=""):
        # Inicializa un objeto Cliente con nombre, email y un carrito vacío.
        self.nombre = nombre
        self.email = email
        self.carrito = []

    def agregar_al_carrito(self, producto, cantidad):
        # Agrega un producto al carrito si hay suficiente stock.
        if producto.stock >= cantidad:
            self.carrito.append((producto, cantidad))
            producto.actualizar_stock(-cantidad)
            print(f"{self.nombre} ha agregado {cantidad} unidades de {producto.nombre} al carrito.")
        else:
            print(f"No hay suficiente stock de {producto.nombre}.")

    def ver_carrito(self):
        # Muestra los productos en el carrito del cliente.
        print(f"Carrito de {self.nombre}:")
        for item in self.carrito:
            producto, cantidad = item
            print(f"{cantidad} x {producto.nombre} - ${producto.precio * cantidad:.2f}")

    def __str__(self):
        # Retorna una representación en cadena del cliente.
        return f"Cliente: {self.nombre}"


class Pedido:
    def __init__(self, cliente):
        # Inicializa un objeto Pedido con el cliente y una copia del carrito del cliente.
        self.cliente = cliente
        self.productos = [(producto, cantidad) for producto, cantidad in cliente.carrito]
        self.total = sum(producto.precio * cantidad for producto, cantidad in self.productos)

    def resumen_pedido(self):
        # Muestra un resumen del pedido.
        print(f"Resumen del pedido para {self.cliente.nombre}:")
        for producto, cantidad in self.productos:
            print(f"{cantidad} x {producto.nombre} - ${producto.precio * cantidad:.2f}")
        print(f"Total a pagar: ${self.total:.2f}")

    def __str__(self):
        # Retorna una representación en cadena del pedido.
        return f"Pedido de {self.cliente.nombre}, Total: ${self.total:.2f}"


# Ejemplo de uso
if __name__ == "__main__":
    # Crear productos
    producto1 = Producto("Laptop", 1200.00, 10)  # Crea un producto Laptop con precio 1200 y stock 10.
    producto2 = Producto("Smartphone", 800.00, 20)  # Crea un producto Smartphone con precio 800 y stock 20.
    producto3 = Producto("Tablet", 300.00, 15)  # Crea un producto Tablet con precio 300 y stock 15.

    # Crear cliente
    cliente = Cliente("Ana Gómez")  # Crea un cliente con nombre Ana Gómez.

    # Cliente agrega productos al carrito
    cliente.agregar_al_carrito(producto1, 1)  # Ana agrega 1 Laptop al carrito.
    cliente.agregar_al_carrito(producto2, 2)  # Ana agrega 2 Smartphones al carrito.

    # Ver carrito
    cliente.ver_carrito()  # Muestra los productos en el carrito de Ana.

    # Crear pedido
    pedido = Pedido(cliente)  # Crea un pedido para Ana con los productos en su carrito.

    # Resumen del pedido
    pedido.resumen_pedido()  # Muestra el resumen del pedido de Ana.

