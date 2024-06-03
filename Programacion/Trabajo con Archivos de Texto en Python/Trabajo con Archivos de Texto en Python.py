# Crea un nuevo archivo llamado my_notes.txt.
my_notes = open('my_notes.txt', 'w')

# Método write(): escribir una línea a la vez
my_notes.write("Estas son mis notas personales:\n")
my_notes.write("1. Recordar comprar leche en el supermercado.\n")
my_notes.write("2. Llamar a mamá para su cumpleaños.\n")
my_notes.write("3. Terminar el proyecto de Python antes del viernes.\n")

# Método writelines(): escribir una lista de líneas
lineas = ["Agrega una lista de notas personales adicionales.\n", "4. Preparar el informe para la reunión del equipo.\n", "5. Hacer ejercicio al menos 30 minutos al día.\n"]
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