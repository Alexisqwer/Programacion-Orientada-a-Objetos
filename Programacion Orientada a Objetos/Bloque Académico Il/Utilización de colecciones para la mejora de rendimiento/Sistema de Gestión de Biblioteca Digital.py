import os
import json


class Libro:
    def __init__(self, titulo, autor, categoria, ISBN):
        self._titulo_autor = (titulo, autor)
        self._categoria = categoria
        self._ISBN = ISBN

    def get_titulo(self):
        return self._titulo_autor[0]

    def get_autor(self):
        return self._titulo_autor[1]

    def get_categoria(self):
        return self._categoria

    def get_ISBN(self):
        return self._ISBN

    def to_dict(self):
        """Convierte el libro en un diccionario para almacenarlo en un archivo JSON."""
        return {
            'titulo': self.get_titulo(),
            'autor': self.get_autor(),
            'categoria': self._categoria,
            'ISBN': self._ISBN
        }

    @classmethod
    def from_dict(cls, data):
        """Crea un objeto Libro a partir de un diccionario."""
        return cls(data['titulo'], data['autor'], data['categoria'], data['ISBN'])

    def __str__(self):
        return f"Titulo: {self.get_titulo()}, Autor: {self.get_autor()}, Categoría: {self.get_categoria()}, ISBN: {self.get_ISBN()}"


class Usuario:
    def __init__(self, nombre, ID_usuario):
        self._nombre = nombre
        self._ID_usuario = ID_usuario
        self._libros_prestados = []

    def get_nombre(self):
        return self._nombre

    def get_ID_usuario(self):
        return self._ID_usuario

    def prestar_libro(self, libro):
        self._libros_prestados.append(libro)

    def devolver_libro(self, ISBN):
        for libro in self._libros_prestados:
            if libro.get_ISBN() == ISBN:
                self._libros_prestados.remove(libro)
                return libro
        return None

    def listar_libros_prestados(self):
        return self._libros_prestados

    def to_dict(self):
        """Convierte el usuario en un diccionario para almacenarlo en un archivo JSON."""
        return {
            'nombre': self._nombre,
            'ID_usuario': self._ID_usuario,
            'libros_prestados': [libro.to_dict() for libro in self._libros_prestados]
        }

    @classmethod
    def from_dict(cls, data):
        """Crea un objeto Usuario a partir de un diccionario."""
        usuario = cls(data['nombre'], data['ID_usuario'])
        usuario._libros_prestados = [Libro.from_dict(libro) for libro in data['libros_prestados']]
        return usuario

    def __str__(self):
        return f"Usuario: {self.get_nombre()}, ID: {self.get_ID_usuario()}, Libros prestados: {len(self._libros_prestados)}"


class Biblioteca:
    def __init__(self, archivo_libros="libros.json", archivo_usuarios="usuarios.json"):
        self.archivo_libros = archivo_libros
        self.archivo_usuarios = archivo_usuarios
        self.libros_disponibles = {}
        self.usuarios_registrados = {}
        self.cargar_libros()
        self.cargar_usuarios()

    def cargar_libros(self):
        """Carga los libros desde un archivo JSON al iniciar el sistema."""
        if os.path.exists(self.archivo_libros):
            with open(self.archivo_libros, "r") as file:
                libros = json.load(file)
                self.libros_disponibles = {libro['ISBN']: Libro.from_dict(libro) for libro in libros}
            print("Libros cargados desde el archivo JSON.")
        else:
            print("No se encontró el archivo de libros. Se creará uno nuevo al añadir un libro.")

    def guardar_libros(self):
        """Guarda todos los libros en un archivo JSON."""
        with open(self.archivo_libros, "w") as file:
            json.dump([libro.to_dict() for libro in self.libros_disponibles.values()], file, indent=4)
        print("Libros guardados en el archivo JSON.")

    def cargar_usuarios(self):
        """Carga los usuarios desde un archivo JSON al iniciar el sistema."""
        if os.path.exists(self.archivo_usuarios):
            with open(self.archivo_usuarios, "r") as file:
                usuarios = json.load(file)
                self.usuarios_registrados = {usuario['ID_usuario']: Usuario.from_dict(usuario) for usuario in usuarios}
            print("Usuarios cargados desde el archivo JSON.")
        else:
            print("No se encontró el archivo de usuarios. Se creará uno nuevo al registrar un usuario.")

    def guardar_usuarios(self):
        """Guarda todos los usuarios en un archivo JSON."""
        with open(self.archivo_usuarios, "w") as file:
            json.dump([usuario.to_dict() for usuario in self.usuarios_registrados.values()], file, indent=4)
        print("Usuarios guardados en el archivo JSON.")

    def añadir_libro(self, libro):
        if libro.get_ISBN() in self.libros_disponibles:
            print("El libro ya está en la biblioteca.")
        else:
            self.libros_disponibles[libro.get_ISBN()] = libro
            self.guardar_libros()
            print("Libro añadido y guardado con éxito.")

    def quitar_libro(self, ISBN):
        if ISBN in self.libros_disponibles:
            del self.libros_disponibles[ISBN]
            self.guardar_libros()
            print("Libro eliminado con éxito.")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.get_ID_usuario() in self.usuarios_registrados:
            print("El usuario ya está registrado.")
        else:
            self.usuarios_registrados[usuario.get_ID_usuario()] = usuario
            self.guardar_usuarios()
            print("Usuario registrado con éxito.")

    def dar_baja_usuario(self, ID_usuario):
        if ID_usuario in self.usuarios_registrados:
            del self.usuarios_registrados[ID_usuario]
            self.guardar_usuarios()
            print("Usuario dado de baja con éxito.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, ISBN, ID_usuario):
        if ISBN not in self.libros_disponibles:
            print("El libro no está disponible.")
        elif ID_usuario not in self.usuarios_registrados:
            print("El usuario no está registrado.")
        else:
            libro = self.libros_disponibles.pop(ISBN)
            usuario = self.usuarios_registrados[ID_usuario]
            usuario.prestar_libro(libro)
            self.guardar_libros()
            self.guardar_usuarios()
            print(f"Libro '{libro.get_titulo()}' prestado a {usuario.get_nombre()}.")

    def devolver_libro(self, ISBN, ID_usuario):
        if ID_usuario not in self.usuarios_registrados:
            print("El usuario no está registrado.")
        else:
            usuario = self.usuarios_registrados[ID_usuario]
            libro = usuario.devolver_libro(ISBN)
            if libro:
                self.libros_disponibles[ISBN] = libro
                self.guardar_libros()
                self.guardar_usuarios()
                print(f"Libro '{libro.get_titulo()}' devuelto con éxito.")
            else:
                print("El usuario no tiene este libro prestado.")

    def buscar_libros(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros_disponibles.values():
            if titulo and titulo.lower() in libro.get_titulo().lower():
                resultados.append(libro)
            elif autor and autor.lower() in libro.get_autor().lower():
                resultados.append(libro)
            elif categoria and categoria.lower() == libro.get_categoria().lower():
                resultados.append(libro)

        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros que coincidan con la búsqueda.")

    def listar_libros_prestados(self, ID_usuario):
        if ID_usuario not in self.usuarios_registrados:
            print("El usuario no está registrado.")
        else:
            usuario = self.usuarios_registrados[ID_usuario]
            libros = usuario.listar_libros_prestados()
            if libros:
                for libro in libros:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")

    def listar_libros(self):
        if not self.libros_disponibles:
            print("No hay libros disponibles en la biblioteca.")
        else:
            for libro in self.libros_disponibles.values():
                print(libro)


def menu():
    biblioteca = Biblioteca()

    while True:
        print("\nMenú de Biblioteca:")
        print("1. Añadir nuevo libro")
        print("2. Quitar libro por ISBN")
        print("3. Registrar nuevo usuario")
        print("4. Dar de baja a un usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libros")
        print("8. Listar libros prestados por usuario")
        print("9. Listar todos los libros disponibles")
        print("10. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            titulo = input("Ingresa el título del libro: ")
            autor = input("Ingresa el autor del libro: ")
            categoria = input("Ingresa la categoría del libro: ")
            ISBN = input("Ingresa el ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, ISBN)
            biblioteca.añadir_libro(libro)

        elif opcion == '2':
            ISBN = input("Ingresa el ISBN del libro a quitar: ")
            biblioteca.quitar_libro(ISBN)

        elif opcion == '3':
            nombre = input("Ingresa el nombre del usuario: ")
            ID_usuario = input("Ingresa el ID del usuario: ")
            usuario = Usuario(nombre, ID_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == '4':
            ID_usuario = input("Ingresa el ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(ID_usuario)

        elif opcion == '5':
            ISBN = input("Ingresa el ISBN del libro a prestar: ")
            ID_usuario = input("Ingresa el ID del usuario: ")
            biblioteca.prestar_libro(ISBN, ID_usuario)

        elif opcion == '6':
            ISBN = input("Ingresa el ISBN del libro a devolver: ")
            ID_usuario = input("Ingresa el ID del usuario: ")
            biblioteca.devolver_libro(ISBN, ID_usuario)

        elif opcion == '7':
            print("Criterios de búsqueda:")
            print("1. Título")
            print("2. Autor")
            print("3. Categoría")
            criterio = input("Selecciona un criterio: ")
            if criterio == '1':
                titulo = input("Ingresa el título a buscar: ")
                biblioteca.buscar_libros(titulo=titulo)
            elif criterio == '2':
                autor = input("Ingresa el autor a buscar: ")
                biblioteca.buscar_libros(autor=autor)
            elif criterio == '3':
                categoria = input("Ingresa la categoría a buscar: ")
                biblioteca.buscar_libros(categoria=categoria)
            else:
                print("Criterio no válido.")

        elif opcion == '8':
            ID_usuario = input("Ingresa el ID del usuario: ")
            biblioteca.listar_libros_prestados(ID_usuario)

        elif opcion == '9':
            biblioteca.listar_libros()

        elif opcion == '10':
            print("Saliendo del sistema de biblioteca.")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu()
