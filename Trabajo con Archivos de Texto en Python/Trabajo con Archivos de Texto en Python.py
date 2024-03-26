# Whiteboard

# Crea un nuevo archivo llamado my_notes.txt.
my_notes = open('my_notes.txt', 'w')

# Método write(): escribir una línea a la vez
my_notes.write("Línea 1: Esto es una prueba.\n")
my_notes.write("Línea 2: Escribiendo en archivos con Python.\n")

# Método writelines(): escribir una lista de líneas
lineas = ["Línea 3: Otro ejemplo.\n", "Línea 4: Finalizando el ejemplo.\n"]
my_notes.writelines(lineas)

# Abre el archivo my_notes.txt.
my_notes = open('my_notes.txt', 'r')

#Lee el contenido del archivo línea por línea utilizando el método adecuado.

# Método 1. read()
print('Método 1: read()')
print('--------------------')
print(my_notes.read())
my_notes.close()

# Método 2. readlines()
my_notes = open('my_notes.txt', 'r')
print('Método 2: readlines()')
print('--------------------')
for linea in my_notes.readlines():
    print(linea.rstrip('\n'))
my_notes.close()