# Definir una función para imprimir los detalles del registro
def imprimir_detalles_del_registro(detalles_del_registro):
    """
    Esta función recibe un diccionario con los detalles del registro
    y los imprime de manera formateada.
    """
    # Imprimir cada detalle del registro usando el diccionario proporcionado
    print(f"ID: {detalles_del_registro['id']}")
    print(f"Nombre: {detalles_del_registro['nombre']}")
    print(f"Edad: {detalles_del_registro['edad']}")
    print(f"Salario: {detalles_del_registro['salario']:.2f}")
    print(f"Activo: {detalles_del_registro['activo']}")

# Crear una función principal para ejecutar el programa
def main():
    """
    Función principal que gestiona el flujo del programa.
    """
    # Crear un diccionario para almacenar la información del registro
    detalles_del_registro = {
        'id': 1,                    # Identificador único del registro (integer)
        'nombre': 'Juan Perez',     # Nombre completo de la persona (string)
        'edad': 30,                 # Edad de la persona (integer)
        'salario': 45000.50,        # Salario de la persona (float)
        'activo': True              # Estado de actividad del registro (boolean)
    }

    # Llamar a la función para imprimir los detalles del registro
    imprimir_detalles_del_registro(detalles_del_registro)

# Verificar si el script se está ejecutando directamente
if __name__ == "__main__":
    main()  # Llamar a la función principal
