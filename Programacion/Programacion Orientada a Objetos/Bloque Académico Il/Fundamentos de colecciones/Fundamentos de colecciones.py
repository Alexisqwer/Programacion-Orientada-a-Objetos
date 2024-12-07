import os
import json


class Producto:
    def __init__(self, ID, nombre, cantidad, precio):
        # Constructor de la clase Producto que inicializa ID, nombre, cantidad y precio
        self.ID = ID
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Representación en cadena del objeto Producto
        return f"ID: {self.ID}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def to_dict(self):
        """Convierte el objeto Producto en un diccionario para guardarlo en un archivo JSON."""
        return {
            'ID': self.ID,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }

    @classmethod
    def from_dict(cls, data):
        """Crea un objeto Producto a partir de un diccionario."""
        return cls(data['ID'], data['nombre'], data['cantidad'], data['precio'])


class Inventario:
    def __init__(self, archivo='inventario.json'):
        # Constructor de la clase Inventario que inicializa un diccionario para productos y el archivo JSON
        self.productos = {}  # Usamos un diccionario para almacenar productos por ID
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde un archivo JSON al iniciar el programa."""
        if os.path.exists(self.archivo):
            try:
                # Intenta abrir el archivo y cargar los datos JSON
                with open(self.archivo, 'r') as file:
                    productos_data = json.load(file)
                    # Convierte los datos JSON en objetos Producto y los almacena en el diccionario
                    self.productos = {ID: Producto.from_dict(data) for ID, data in productos_data.items()}
            except (FileNotFoundError, PermissionError, json.JSONDecodeError) as e:
                # Maneja posibles errores al cargar el archivo
                print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda todos los productos en un archivo JSON."""
        try:
            # Intenta abrir el archivo y guardar los productos en formato JSON
            with open(self.archivo, 'w') as file:
                productos_data = {ID: producto.to_dict() for ID, producto in self.productos.items()}
                json.dump(productos_data, file, indent=4)
        except (FileNotFoundError, PermissionError) as e:
            # Maneja posibles errores al guardar el archivo
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        """Añade un nuevo producto al inventario."""
        if producto.ID in self.productos:
            # Verifica si el ID ya existe en el inventario
            print("Error: El ID del producto ya existe.")
        else:
            # Añade el producto al diccionario y guarda el inventario
            self.productos[producto.ID] = producto
            self.guardar_inventario()
            print("Producto añadido con éxito.")

    def eliminar_producto(self, ID):
        """Elimina un producto del inventario por su ID."""
        if ID in self.productos:
            # Verifica si el producto existe y lo elimina
            del self.productos[ID]
            self.guardar_inventario()
            print("Producto eliminado con éxito.")
        else:
            # Mensaje de error si el producto no se encuentra
            print("Error: No se encontró el producto con el ID proporcionado.")

    def actualizar_producto(self, ID, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto por su ID."""
        if ID in self.productos:
            # Verifica si el producto existe y actualiza la cantidad o el precio
            if cantidad is not None:
                self.productos[ID].cantidad = cantidad
            if precio is not None:
                self.productos[ID].precio = precio
            self.guardar_inventario()
            print("Producto actualizado con éxito.")
        else:
            # Mensaje de error si el producto no se encuentra
            print("Error: No se encontró el producto con el ID proporcionado.")

    def buscar_productos(self, nombre):
        """Busca y muestra productos por nombre."""
        # Busca productos que contengan el nombre proporcionado (insensible a mayúsculas/minúsculas)
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.nombre.lower()]
        if resultados:
            # Muestra los productos encontrados
            for producto in resultados:
                print(producto)
        else:
            # Mensaje si no se encontraron productos
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        """Muestra todos los productos en el inventario."""
        if self.productos:
            # Muestra todos los productos si hay alguno en el inventario
            for producto in self.productos.values():
                print(producto)
        else:
            # Mensaje si el inventario está vacío
            print("No hay productos en el inventario.")


def menu():
    inventario = Inventario()

    while True:
        # Menú de opciones para el usuario
        print("\nMenú de Inventario:")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto por ID")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos en el inventario")
        print("6. Guardar y Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            # Opción para añadir un nuevo producto
            ID = input("Ingresa el ID del producto: ")
            nombre = input("Ingresa el nombre del producto: ")
            cantidad = int(input("Ingresa la cantidad del producto: "))
            precio = float(input("Ingresa el precio del producto: "))
            producto = Producto(ID, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            # Opción para eliminar un producto por ID
            ID = input("Ingresa el ID del producto a eliminar: ")
            inventario.eliminar_producto(ID)

        elif opcion == '3':
            # Opción para actualizar cantidad o precio de un producto por ID
            ID = input("Ingresa el ID del producto a actualizar: ")
            cantidad = input("Ingresa la nueva cantidad (deja en blanco para no cambiar): ")
            precio = input("Ingresa el nuevo precio (deja en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(ID, cantidad, precio)

        elif opcion == '4':
            # Opción para buscar productos por nombre
            nombre = input("Ingresa el nombre del producto a buscar: ")
            inventario.buscar_productos(nombre)

        elif opcion == '5':
            # Opción para mostrar todos los productos en el inventario
            inventario.mostrar_todos()

        elif opcion == '6':
            # Opción para salir del programa
            print("Guardando y Saliendo del programa...")
            break

        else:
            # Mensaje si se selecciona una opción no válida
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
