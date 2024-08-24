import os

class Producto:
    def __init__(self, ID, nombre, cantidad, precio):
        # Constructor que inicializa los atributos del objeto Producto
        self._ID = ID
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters (Métodos para obtener los valores de los atributos)
    def get_ID(self):
        # Devuelve el valor de _ID
        return self._ID

    def get_nombre(self):
        # Devuelve el valor de _nombre
        return self._nombre

    def get_cantidad(self):
        # Devuelve el valor de _cantidad
        return self._cantidad

    def get_precio(self):
        # Devuelve el valor de _precio
        return self._precio

    # Setters (Métodos para modificar los valores de los atributos)
    def set_nombre(self, nombre):
        # Establece un nuevo valor para _nombre
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        # Establece un nuevo valor para _cantidad
        self._cantidad = cantidad

    def set_precio(self, precio):
        # Establece un nuevo valor para _precio
        self._precio = precio

    def __str__(self):
        # Devuelve una representación en cadena del objeto Producto
        return f"ID: {self._ID}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: {self._precio}"

    def to_line(self):
        """Convierte el objeto Producto en una línea de texto para guardarlo en un archivo."""
        # Convierte los atributos del producto en una cadena de texto con formato CSV
        return f"{self._ID},{self._nombre},{self._cantidad},{self._precio}\n"

    @classmethod
    def from_line(cls, line):
        """Crea un objeto Producto a partir de una línea de texto."""
        # Descompone una línea de texto CSV y crea un objeto Producto con los valores obtenidos
        ID, nombre, cantidad, precio = line.strip().split(',')
        return cls(ID, nombre, int(cantidad), float(precio))


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        # Constructor que inicializa la lista de productos y carga los datos desde un archivo
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo al iniciar el programa."""
        # Verifica si el archivo existe para cargar los productos desde él
        if os.path.exists(self.archivo):
            try:
                # Abre el archivo en modo lectura y lee línea por línea
                with open(self.archivo, 'r') as file:
                    for line in file:
                        # Crea un objeto Producto a partir de cada línea y lo añade a la lista de productos
                        producto = Producto.from_line(line)
                        self.productos.append(producto)
            except (FileNotFoundError, PermissionError) as e:
                # Captura y muestra errores si el archivo no se encuentra o no se puede abrir
                print(f"Error al cargar el inventario: {e}")
        else:
            # Si el archivo no existe, lo crea vacío
            open(self.archivo, 'w').close()

    def guardar_inventario(self):
        """Guarda todos los productos en el archivo."""
        try:
            # Abre el archivo en modo escritura para guardar todos los productos
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    # Convierte cada producto a una línea de texto y la escribe en el archivo
                    file.write(producto.to_line())
        except (FileNotFoundError, PermissionError) as e:
            # Captura y muestra errores si el archivo no se encuentra o no se puede abrir
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        # Verifica que el ID del nuevo producto sea único
        for p in self.productos:
            if p.get_ID() == producto.get_ID():
                # Si el ID ya existe, muestra un mensaje de error y no añade el producto
                print("Error: El ID del producto ya existe.")
                return
        # Si el ID es único, añade el producto a la lista y guarda el inventario en el archivo
        self.productos.append(producto)
        self.guardar_inventario()
        print("Producto añadido con éxito.")

    def eliminar_producto(self, ID):
        # Busca el producto con el ID proporcionado
        for producto in self.productos:
            if producto.get_ID() == ID:
                # Si encuentra el producto, lo elimina de la lista y guarda el inventario
                self.productos.remove(producto)
                self.guardar_inventario()
                print("Producto eliminado con éxito.")
                return
        # Si no encuentra el producto, muestra un mensaje de error
        print("Error: No se encontró el producto con el ID proporcionado.")

    def actualizar_producto(self, ID, cantidad=None, precio=None):
        # Busca el producto con el ID proporcionado
        for producto in self.productos:
            if producto.get_ID() == ID:
                # Si se proporcionó una nueva cantidad, la actualiza
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                # Si se proporcionó un nuevo precio, lo actualiza
                if precio is not None:
                    producto.set_precio(precio)
                # Guarda los cambios en el inventario
                self.guardar_inventario()
                print("Producto actualizado con éxito.")
                return
        # Si no encuentra el producto, muestra un mensaje de error
        print("Error: No se encontró el producto con el ID proporcionado.")

    def buscar_productos(self, nombre):
        # Busca productos cuyo nombre contenga la cadena proporcionada
        resultados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        if resultados:
            # Si encuentra productos, los muestra
            for producto in resultados:
                print(producto)
        else:
            # Si no encuentra productos, muestra un mensaje
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        # Muestra todos los productos en el inventario
        if self.productos:
            for producto in self.productos:
                print(producto)
        else:
            # Si no hay productos, muestra un mensaje indicando que el inventario está vacío
            print("No hay productos en el inventario.")


def menu():
    # Crea una instancia de Inventario
    inventario = Inventario()

    while True:
        # Muestra el menú de opciones al usuario
        print("\nMenú de Inventario:")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto por ID")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos en el inventario")
        print("6. Salir")

        # Solicita al usuario que elija una opción
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            # Si elige añadir un producto, solicita los datos necesarios
            ID = input("Ingresa el ID del producto: ")
            nombre = input("Ingresa el nombre del producto: ")
            cantidad = int(input("Ingresa la cantidad del producto: "))
            precio = float(input("Ingresa el precio del producto: "))
            # Crea un nuevo producto y lo añade al inventario
            producto = Producto(ID, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            # Si elige eliminar un producto, solicita el ID del producto a eliminar
            ID = input("Ingresa el ID del producto a eliminar: ")
            inventario.eliminar_producto(ID)

        elif opcion == '3':
            # Si elige actualizar un producto, solicita el ID y los nuevos valores
            ID = input("Ingresa el ID del producto a actualizar: ")
            cantidad = input("Ingresa la nueva cantidad (deja en blanco para no cambiar): ")
            precio = input("Ingresa el nuevo precio (deja en blanco para no cambiar): ")
            # Convierte los valores ingresados a los tipos adecuados
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            # Actualiza el producto en el inventario
            inventario.actualizar_producto(ID, cantidad, precio)

        elif opcion == '4':
            # Si elige buscar un producto, solicita el nombre a buscar
            nombre = input("Ingresa el nombre del producto a buscar: ")
            inventario.buscar_productos(nombre)

        elif opcion == '5':
            # Si elige mostrar todos los productos, los lista
            inventario.mostrar_todos()

        elif opcion == '6':
            # Si elige salir, finaliza el bucle y sale del programa
            print("Saliendo del programa...")
            break

        else:
            # Si la opción ingresada no es válida, muestra un mensaje de error
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()  # Llama a la función menu si el archivo se ejecuta como script principal
