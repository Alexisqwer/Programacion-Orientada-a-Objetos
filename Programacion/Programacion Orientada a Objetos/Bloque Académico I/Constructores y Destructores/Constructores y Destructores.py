class Libro:
    def __init__(self, titulo, autor):
        """
        Constructor para inicializar los atributos del objeto Libro.
        """
        self.titulo = titulo  # Asigna el título del libro
        self.autor = autor    # Asigna el autor del libro
        print(f"Libro '{self.titulo}' de {self.autor} ha sido creado.")  # Imprime un mensaje al crear un libro

    def __del__(self):
        """
        Destructor para realizar la limpieza cuando el objeto Libro es destruido.
        """
        print(f"Libro '{self.titulo}' de {self.autor} ha sido eliminado.")  # Imprime un mensaje al eliminar un libro

class Biblioteca:
    def __init__(self):
        """
        Constructor para inicializar la lista de libros en la biblioteca.
        """
        self.libros = []  # Inicializa una lista vacía para almacenar libros
        print("Biblioteca creada.")  # Imprime un mensaje al crear una biblioteca

    def agregar_libro(self, libro):
        """
        Método para agregar un libro a la biblioteca.
        """
        self.libros.append(libro)  # Agrega el libro a la lista de libros
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")  # Imprime un mensaje al agregar un libro

    def eliminar_libro(self, titulo):
        """
        Método para eliminar un libro de la biblioteca por su título.
        """
        for libro in self.libros:  # Itera sobre los libros en la biblioteca
            if libro.titulo == titulo:  # Verifica si el título coincide
                self.libros.remove(libro)  # Remueve el libro de la lista
                del libro  # Elimina el objeto libro
                print(f"Libro '{titulo}' eliminado de la biblioteca.")  # Imprime un mensaje al eliminar un libro
                return
        print(f"Libro '{titulo}' no encontrado en la biblioteca.")  # Imprime un mensaje si el libro no es encontrado

    def listar_libros(self):
        """
        Método para listar todos los libros en la biblioteca.
        """
        if not self.libros:  # Verifica si la lista de libros está vacía
            print("La biblioteca está vacía.")  # Imprime un mensaje si la biblioteca está vacía
        else:
            print("Libros en la biblioteca:")  # Imprime un encabezado para la lista de libros
            for libro in self.libros:  # Itera sobre los libros en la biblioteca
                print(f"- {libro.titulo} de {libro.autor}")  # Imprime los detalles de cada libro

# Código principal
def main():
    """
    Función principal que gestiona el flujo del programa.
    """
    # Crear una biblioteca
    biblioteca = Biblioteca()  # Crea una instancia de la biblioteca

    # Crear algunos libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez")  # Crea un libro
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes")  # Crea otro libro
    libro3 = Libro("La Sombra del Viento", "Carlos Ruiz Zafón")  # Crea otro libro

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)  # Agrega el primer libro a la biblioteca
    biblioteca.agregar_libro(libro2)  # Agrega el segundo libro a la biblioteca
    biblioteca.agregar_libro(libro3)  # Agrega el tercer libro a la biblioteca

    # Listar libros en la biblioteca
    biblioteca.listar_libros()  # Lista los libros en la biblioteca

    # Eliminar un libro de la biblioteca
    biblioteca.eliminar_libro("Don Quijote de la Mancha")  # Elimina un libro específico de la biblioteca

    # Listar libros nuevamente para verificar la eliminación
    biblioteca.listar_libros()  # Lista los libros nuevamente para verificar que el libro fue eliminado

if __name__ == "__main__":
    main()  # Llamar a la función principal

