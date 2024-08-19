import os

class Producto:
    def __init__(self, ID, nombre, cantidad, precio):
        self._ID = ID
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_ID(self):
        return self._ID

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"ID: {self._ID}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}"

    def to_line(self):
        """Convierte el objeto Producto en una línea de texto para guardarlo en un archivo."""
        return f"{self._ID},{self._nombre},{self._cantidad},{self._precio}\n"

    @classmethod
    def from_line(cls, line):
        """Crea un objeto Producto a partir de una línea de texto."""
        ID, nombre, cantidad, precio = line.strip().split(',')
        return cls(ID, nombre, int(cantidad), float(precio))


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo al iniciar el programa."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    for line in file:
                        producto = Producto.from_line(line)
                        self.productos.append(producto)
            except (FileNotFoundError, PermissionError) as e:
                print(f"Error al cargar el inventario: {e}")
        else:
            # Si el archivo no existe, se crea un archivo vacío
            open(self.archivo, 'w').close()

    def guardar_inventario(self):
        """Guarda todos los productos en el archivo."""
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(producto.to_line())
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        # Verificar que el ID sea único
        for p in self.productos:
            if p.get_ID() == producto.get_ID():
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        self.guardar_inventario()
        print("Producto añadido con éxito.")

    def eliminar_producto(self, ID):
        for producto in self.productos:
            if producto.get_ID() == ID:
                self.productos.remove(producto)
                self.guardar_inventario()
                print("Producto eliminado con éxito.")
                return
        print("Error: No se encontró el producto con el ID proporcionado.")

    def actualizar_producto(self, ID, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_ID() == ID:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                self.guardar_inventario()
                print("Producto actualizado con éxito.")
                return
        print("Error: No se encontró el producto con el ID proporcionado.")

    def buscar_productos(self, nombre):
        resultados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            print("No hay productos en el inventario.")


def menu():
    inventario = Inventario()

    while True:
        print("\nMenú de Inventario:")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto por ID")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos en el inventario")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            ID = input("Ingresa el ID del producto: ")
            nombre = input("Ingresa el nombre del producto: ")
            cantidad = int(input("Ingresa la cantidad del producto: "))
            precio = float(input("Ingresa el precio del producto: "))
            producto = Producto(ID, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            ID = input("Ingresa el ID del producto a eliminar: ")
            inventario.eliminar_producto(ID)

        elif opcion == '3':
            ID = input("Ingresa el ID del producto a actualizar: ")
            cantidad = input("Ingresa la nueva cantidad (deja en blanco para no cambiar): ")
            precio = input("Ingresa el nuevo precio (deja en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(ID, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingresa el nombre del producto a buscar: ")
            inventario.buscar_productos(nombre)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
