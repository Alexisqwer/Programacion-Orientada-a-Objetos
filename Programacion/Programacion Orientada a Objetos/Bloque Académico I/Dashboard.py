import os
import subprocess

# Constantes
# Define un diccionario que asigna opciones de menú a nombres de directorios
MENU_OPTIONS = {
    '1': 'Técnicas de Programación',
    '2': 'Programacion tradicional frente a POO',
    '3': 'EjemplosMundoReal_POO',
    '4': 'Tipos de datos, Identificadores',
    '5': 'Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo',
    '6': 'Constructores y Destructores',
}


# Función para mostrar el código de un script de Python
def mostrar_codigo(ruta_script):
    """Muestra el contenido de un archivo de script en la consola."""
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al abrir el archivo: {e}")


# Función para mostrar el contenido de un directorio
def mostrar_contenido_carpeta(ruta_carpeta):
    """Muestra el contenido de una carpeta."""
    print(f"\nContenido de la carpeta {ruta_carpeta}:")
    for elemento in os.listdir(ruta_carpeta):
        ruta_elemento = os.path.join(ruta_carpeta, elemento)
        if os.path.isdir(ruta_elemento):
            print(f"  Carpeta: {elemento}")
        else:
            print(f"  Archivo: {elemento}")


# Función para ejecutar un script de Python
def ejecutar_archivo_python(ruta_archivo):
    """Cambia el directorio actual al del archivo y ejecuta el archivo Python."""
    os.chdir(os.path.dirname(ruta_archivo))
    subprocess.run(['python', ruta_archivo])


# Función del menú principal
def mostrar_menu():
    """Muestra el menú principal y maneja la interacción con el usuario."""
    # Obtiene el directorio base del script
    ruta_base = os.path.dirname(os.path.realpath(__file__))

    while True:
        # Muestra el menú principal
        print("\nMenu Principal - Dashboard")
        for key, value in MENU_OPTIONS.items():
            # Itera sobre las opciones del menú
            print(f"{key} - {value}")
        print("0 - salir")

        # Obtiene la entrada del usuario
        eleccion = input("Escribe una opción: para salir ")
        if eleccion == '0':
            # Sale del programa si el usuario elige salir
            break
        elif eleccion in MENU_OPTIONS:
            # Obtiene la ruta del directorio correspondiente a la opción del menú seleccionada
            ruta_carpeta = os.path.join(ruta_base, MENU_OPTIONS[eleccion])
            if os.path.isdir(ruta_carpeta):
                # Muestra el contenido del directorio
                mostrar_contenido_carpeta(ruta_carpeta)

                # Pregunta al usuario si desea ejecutar los scripts de Python en el directorio
                respuesta = input("¿Desea ejecutar los archivos Python en la carpeta? (s/n): ")
                if respuesta.lower() == 's':
                    # Encuentra todos los archivos Python en el directorio
                    archivos_python = [f for f in os.listdir(ruta_carpeta) if f.endswith('.py')]
                    if archivos_python:
                        # Ejecuta cada archivo Python
                        for archivo_python in archivos_python:
                            ruta_archivo = os.path.join(ruta_carpeta, archivo_python)
                            print(f"\nEjecutando archivo {archivo_python}...")
                            ejecutar_archivo_python(ruta_archivo)
                            print(f"Archivo {archivo_python} ejecutado correctamente.")
                    else:
                        print("No se encontró ningún archivo Python en la carpeta.")
            else:
                print(f"La carpeta {MENU_OPTIONS[eleccion]} no existe.")
        else:
            print("Opción no válida. Por favor, intente de nuevo")


# Ejecuta la función del menú principal si el script se ejecuta directamente
if __name__ == '__main__':
    mostrar_menu()
