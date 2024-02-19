def ordenar_fila(matriz, numero_fila):
    # Verificar si la fila está dentro del rango válido
    if 0 <= numero_fila < len(matriz):
        # Ordenar la fila usando el algoritmo de ordenación (Bubble Sort en este caso)
        matriz[numero_fila] = bubble_sort(matriz[numero_fila])

def bubble_sort(fila):
    n = len(fila)

    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

    return fila

# Definir una matriz de ejemplo 3x3
matriz_ejemplo = [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]

# Mostrar la matriz original
print("Matriz Original:")
for fila in matriz_ejemplo:
    print(fila)

# Ordenar la fila 1 (índice 0) en orden ascendente
numero_fila_a_ordenar = 1
ordenar_fila(matriz_ejemplo, numero_fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con Fila Ordenada:")
for fila in matriz_ejemplo:
    print(fila)
