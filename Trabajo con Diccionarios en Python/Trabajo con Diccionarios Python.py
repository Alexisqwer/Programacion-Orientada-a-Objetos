# Crear el diccionario informacion_personal con información ficticia
informacion_personal = {
    "nombre": "Alexis",
    "edad": 19,
    "ciudad": "Pastaza",
    "profesion": "Ingeniero en tegnologias de la informacion"
}

# Acceder y modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Puyo"

# Agregar una nueva clave-valor al diccionario que represente la "profesion" de la persona
informacion_personal["profesion"] = "Programador"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593 95 882 7754"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)