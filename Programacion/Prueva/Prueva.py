import threading
import time

# Definimos una función que será ejecutada por cada hilo
def print_numbers():
    for i in range(10):
        print(f"Hilo {threading.current_thread().name} - Número: {i}")
        time.sleep(1)  # Simula una tarea que toma tiempo

def print_letters():
    for letter in 'ABCDEFGHIJ':
        print(f"Hilo {threading.current_thread().name} - Letra: {letter}")
        time.sleep(1)  # Simula una tarea que toma tiempo

# Creamos dos hilos para ejecutar las funciones definidas anteriormente
hilo1 = threading.Thread(target=print_numbers, name='HiloNumeros')
hilo2 = threading.Thread(target=print_letters, name='HiloLetras')

# Iniciamos los hilos
hilo1.start()
hilo2.start()

# Esperamos a que ambos hilos terminen
hilo1.join()
hilo2.join()

print("Ambos hilos han terminado la ejecución.")

