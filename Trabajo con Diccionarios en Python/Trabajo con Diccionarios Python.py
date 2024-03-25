# Crear el diccionario informacion_personal con información
print("*************************************************")
print("Diccionario con los valores sin modificar")
print("*************************************************")
informacion_personal = {
    "Nombre": "Alexis",
    "Edad": 19,
    "Ciudad": "Puyo",
    "Profesion": "Ingeniero en tegnologias de la informacion"
}
#imprime todos los elementos del diccionario informacion_personal
for key in informacion_personal:
    print(f"{key}: {informacion_personal[key]}")

# Acceder y modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor al diccionario que represente la "profesion" de la persona
informacion_personal["profesion"] = "Programador"
informacion_personal["telefono"]= "095 882 7754"
print("********************************************************")

print(" ")
print("***********************************************")
print("Nuevo diccionario con los valores modificados")
print("***********************************************")

# Verificar si la clave "telefono" existe en el diccionario y agregar
if "telefono" in informacion_personal:
    print("El telefono existe en este diccionario")
else:
    print("El telefono no existe en el diccionario")

# Eliminar la clave "edad" del diccionario
del informacion_personal["Edad"]

# Imprimir el diccionario final
for key in informacion_personal:
    print(f"{key}: {informacion_personal[key]}")
print("***********************************************")
