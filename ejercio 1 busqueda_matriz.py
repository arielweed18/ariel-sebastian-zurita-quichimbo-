def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz"


# Definir una matriz 3x3
matriz = [
    [4, 8, 15],
    [16, 23, 42],
    [1, 9, 27]
]

# Definir el valor a buscar
valor_buscado = int(input("Ingrese el valor a buscar: "))

# Buscar el valor en la matriz
resultado = buscar_valor(matriz, valor_buscado)
print(resultado)
