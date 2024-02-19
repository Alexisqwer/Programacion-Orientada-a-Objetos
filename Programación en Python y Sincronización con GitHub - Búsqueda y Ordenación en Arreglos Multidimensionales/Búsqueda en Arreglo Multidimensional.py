def buscar_valor(matriz, valor):
    # Buscar el valor en la matriz
    for fila_idx, fila in enumerate(matriz):
        for col_idx, elemento in enumerate(fila):
            if elemento == valor:
                return True, (fila_idx, col_idx)  # Se encontró el valor y se devuelve la posición

    return False, None  # El valor no se encontró

# Definir una matriz de ejemplo 3x3
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_a_buscar = 5

# Llamar a la función de búsqueda
encontrado, posicion = buscar_valor(matriz_ejemplo, valor_a_buscar)

# Mostrar resultados
if encontrado:
    print(f"El valor {valor_a_buscar} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
