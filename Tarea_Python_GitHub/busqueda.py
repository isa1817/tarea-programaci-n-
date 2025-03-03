def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posición si encuentra el valor
    return None  # Retorna None si el valor no está en la matriz


# Definir la matriz 3x3
matriz = [
    [4, 8, 15],
    [16, 23, 42],
    [1, 7, 11]
]

# Solicitar al usuario un número a buscar
valor_buscar = int(input("Ingrese el número que desea buscar: "))

# Buscar el valor en la matriz
posicion = buscar_valor(matriz, valor_buscar)

# Mostrar resultado
if posicion:
    print(f"El número {valor_buscar} se encontró en la posición {posicion}.")
else:
    print(f"El número {valor_buscar} no se encuentra en la matriz.")

