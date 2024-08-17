class Producto:
    def __init__(self, ID, nombre, cantidad, precio):
        # Inicializamos los atributos del producto con los valores proporcionados
        self._ID = ID
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_ID(self):
        # Retorna el ID del producto
        return self._ID

    def get_nombre(self):
        # Retorna el nombre del producto
        return self._nombre

    def get_cantidad(self):
        # Retorna la cantidad del producto
        return self._cantidad

    def get_precio(self):
        # Retorna el precio del producto
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        # Permite actualizar el nombre del producto
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        # Permite actualizar la cantidad del producto
        self._cantidad = cantidad

    def set_precio(self, precio):
        # Permite actualizar el precio del producto
        self._precio = precio

    def __str__(self):
        # Devuelve una representación en cadena del producto para facilitar su impresión
        return f"ID: {self._ID}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}"


class Inventario:
    def __init__(self):
        # Inicializamos una lista vacía para almacenar los productos
        self.productos = []

    def añadir_producto(self, producto):
        # Verificar que el ID del nuevo producto sea único
        for p in self.productos:
            if p.get_ID() == producto.get_ID():
                print("Error: El ID del producto ya existe.")
                return
        # Si el ID es único, añadimos el producto a la lista
        self.productos.append(producto)
        print("Producto añadido con éxito.")

    def eliminar_producto(self, ID):
        # Intentamos encontrar y eliminar un producto por su ID
        for producto in self.productos:
            if producto.get_ID() == ID:
                self.productos.remove(producto)
                print("Producto eliminado con éxito.")
                return
        # Si no se encuentra el producto, informamos al usuario
        print("Error: No se encontró el producto con el ID proporcionado.")

    def actualizar_producto(self, ID, cantidad=None, precio=None):
        # Buscamos el producto por ID y actualizamos sus atributos si se encuentran
        for producto in self.productos:
            if producto.get_ID() == ID:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print("Producto actualizado con éxito.")
                return
        # Si no se encuentra el producto, informamos al usuario
        print("Error: No se encontró el producto con el ID proporcionado.")

    def buscar_productos(self, nombre):
        # Buscamos productos cuyo nombre contenga la cadena proporcionada (ignorando mayúsculas)
        resultados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        if resultados:
            # Si se encuentran coincidencias, se imprimen
            for producto in resultados:
                print(producto)
        else:
            # Si no se encuentran coincidencias, informamos al usuario
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        # Imprimimos todos los productos en el inventario
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("No hay productos en el inventario.")


def menu():
    # Creamos una instancia de Inventario para manejar los productos
    inventario = Inventario()

    while True:
        # Menú interactivo para que el usuario elija una acción
        print("\nMenú de Inventario:")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto por ID")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos en el inventario")
        print("6. Salir")

        # Obtenemos la opción del usuario
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            # Añadir un nuevo producto al inventario
            ID = input("Ingresa el ID del producto: ")
            nombre = input("Ingresa el nombre del producto: ")
            cantidad = int(input("Ingresa la cantidad del producto: "))
            precio = float(input("Ingresa el precio del producto: "))
            producto = Producto(ID, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            # Eliminar un producto del inventario por su ID
            ID = input("Ingresa el ID del producto a eliminar: ")
            inventario.eliminar_producto(ID)

        elif opcion == '3':
            # Actualizar la cantidad o el precio de un producto
            ID = input("Ingresa el ID del producto a actualizar: ")
            cantidad = input("Ingresa la nueva cantidad (deja en blanco para no cambiar): ")
            precio = input("Ingresa el nuevo precio (deja en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(ID, cantidad, precio)

        elif opcion == '4':
            # Buscar productos por nombre
            nombre = input("Ingresa el nombre del producto a buscar: ")
            inventario.buscar_productos(nombre)

        elif opcion == '5':
            # Mostrar todos los productos en el inventario
            inventario.mostrar_todos()

        elif opcion == '6':
            # Salir del programa
            print("Saliendo del programa...")
            break

        else:
            # Si el usuario ingresa una opción no válida, se le indica que intente de nuevo
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    # Ejecutamos el menú interactivo al iniciar el programa
    menu()