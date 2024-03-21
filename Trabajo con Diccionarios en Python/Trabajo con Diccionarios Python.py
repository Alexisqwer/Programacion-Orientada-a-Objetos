# Crear el diccionario informacion_personal con información
informacion_personal = {
    "nombre": "Alexis",
    "edad": 19,
    "ciudad": "Puyo",
    "profesion": "Ingeniero en tegnologias de la informacion"
}
#imprime todos los elementos del diccionario informacion_personal
print(informacion_personal)

# Acceder y modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor al diccionario que represente la "profesion" de la persona
informacion_personal["profesion"] = "Programador"
informacion_personal["telefono"]= "+593 95 882 7754"

# Verificar si la clave "telefono" existe en el diccionario y agregar
if "telefono" in informacion_personal:
    print("El telefono existe en el diccionario")
else:
    print("El telefono no existe en el diccionario")

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
