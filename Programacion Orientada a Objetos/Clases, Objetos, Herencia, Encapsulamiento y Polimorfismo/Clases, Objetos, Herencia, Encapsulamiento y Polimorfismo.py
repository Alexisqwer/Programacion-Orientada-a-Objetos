# Programa que demuestra conceptos de POO: herencia, encapsulación y polimorfismo

# Definición de la clase base 'Animal'
class Animal:
    def __init__(self, nombre):
        self._nombre = nombre  # atributo protegido con un solo guion bajo

    def get_nombre(self):
        return self._nombre  # método para obtener el nombre del animal

    def emitir_sonido(self):
        raise NotImplementedError("Método no implementado en la clase base")
        # Método abstracto que debe ser implementado por las clases derivadas

# Definición de la clase derivada 'Perro' que hereda de 'Animal'
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # llama al constructor de la clase base
        self._raza = raza  # atributo protegido con un solo guion bajo

    def get_raza(self):
        return self._raza  # método para obtener la raza del perro

    # Polimorfismo: sobrescribe el método emitir_sonido
    def emitir_sonido(self):
        return "¡Guau!"  # implementación específica para el sonido del perro

# Definición de la clase derivada 'Gato' que hereda de 'Animal'
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)  # llama al constructor de la clase base
        self.__color = color  # atributo privado con dos guiones bajos

    def get_color(self):
        return self.__color  # método para obtener el color del gato

    # Polimorfismo: sobrescribe el método emitir_sonido
    def emitir_sonido(self):
        return "¡Miau!"  # implementación específica para el sonido del gato

# Creación de instancias y demostración de funcionalidad
def main():
    perro = Perro("Bobby", "Labrador")  # instancia de Perro con nombre y raza
    gato = Gato("Garfield", "Naranja")  # instancia de Gato con nombre y color

    # Acceso a métodos y atributos de cada instancia
    print(f"{perro.get_nombre()} es un {perro.get_raza()} que dice: {perro.emitir_sonido()}")
    # Imprime nombre, raza y sonido del perro
    print(f"{gato.get_nombre()} es de color {gato.get_color()} y dice: {gato.emitir_sonido()}")
    # Imprime nombre, color y sonido del gato

if __name__ == "__main__":
    main()  # llama a la función main cuando se ejecuta este script
