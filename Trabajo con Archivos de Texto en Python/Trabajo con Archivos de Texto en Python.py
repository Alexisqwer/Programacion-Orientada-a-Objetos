# Escritura de Archivo de Texto
with open("my_notes.txt", "w") as file:
    # Escribir notas personales en el archivo
    file.write("Estas son mis notas personales:\n")
    file.write("1. Hoy debo completar la tarea de programación.\n")
    file.write("2. Mañana tengo una reunión importante a las 10 a.m.\n")
    file.write("3. No olvidar comprar leche en el camino a casa.\n")

# Lectura de Archivo de Texto
with open("my_notes.txt", "r") as file:
    # Leer y mostrar cada línea del archivo
    print("Contenido de my_notes.txt:")
    for line in file.readlines():
        print(line.strip())  # Eliminar caracteres de nueva línea al imprimir

