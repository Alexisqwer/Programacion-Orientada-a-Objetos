import os
import subprocess

# Constantes
MENU_OPTIONS = {
    '1': 'Técnicas de Programación',
    '2': 'Programacion tradicional frente a POO',
    '3': 'EjemplosMundoReal_POO',
    '4': 'Tipos de datos, Identificadores',
    '5': 'Clases, Objetos, Herencia, Encapsulamiento y Polimorfismo',
    '6': 'Constructores y Destructores',
    '7': 'Dashboard',
}

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al abrir el archivo: {e}")

def mostrar_contenido_carpeta(ruta_carpeta):
    print(f"\nContenido de la carpeta {ruta_carpeta}:")
    for elemento in os.listdir(ruta_carpeta):
        ruta_elemento = os.path.join(ruta_carpeta, elemento)
        if os.path.isdir(ruta_elemento):
            print(f"  Carpeta: {elemento}")
        else:
            print(f"  Archivo: {elemento}")

def ejecutar_archivo_python(ruta_archivo):
    os.chdir(os.path.dirname(ruta_archivo))
    subprocess.run(['python', ruta_archivo])

def mostrar_menu():
    ruta_base = os.path.dirname(os.path.realpath(__file__))
    while True:
        print("\nMenu Principal - Dashboard")
        for key, value in MENU_OPTIONS.items():
            print(f"{key} - {value}")
        print("0 - salir")
        eleccion = input("Escribe una opción: o '0' para salir ")
        if eleccion == '0':
            break
        elif eleccion in MENU_OPTIONS:
            ruta_carpeta = os.path.join(ruta_base, MENU_OPTIONS[eleccion])
            if os.path.isdir(ruta_carpeta):
                mostrar_contenido_carpeta(ruta_carpeta)
                respuesta = input("¿Desea ejecutar los archivos Python en la carpeta? (s/n): ")
                if respuesta.lower() == 's':
                    # Busca los archivos Python en la carpeta seleccionada
                    archivos_python = [f for f in os.listdir(ruta_carpeta) if f.endswith('.py')]
                    if archivos_python:
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

if __name__ == '__main__':
    mostrar_menu()