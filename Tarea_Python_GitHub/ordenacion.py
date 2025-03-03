def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambio de elementos
    return fila


# Definir la matriz 3x3
matriz = [
    [10, 5, 3],
    [8, 12, 4],
    [6, 9, 2]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Especificamos la fila a ordenar (segunda fila, índice 1)
fila_a_ordenar = 1
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
