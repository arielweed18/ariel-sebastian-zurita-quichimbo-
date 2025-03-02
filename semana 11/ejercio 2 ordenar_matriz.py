def ordenar_fila(matriz, fila):
    matriz[fila].sort()  # Ordena la fila usando sort() de Python
    return matriz

# Definir la matriz 3x3
matriz = [
    [5, 8, 2],
    [4, 1, 9],
    [7, 3, 6]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar
fila_a_ordenar = int(input("Ingrese el número de fila (0-2) a ordenar: "))
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

print("\nMatriz después de ordenar la fila:")
for fila in matriz_ordenada:
    print(fila)