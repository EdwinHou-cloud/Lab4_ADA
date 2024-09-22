def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = int(input(f"Ingrese el valor para la posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    # Encuentra el número máximo de dígitos para un mejor formato
    max_digitos = max(len(str(num)) for fila in matriz for num in fila)
    
    for fila in matriz:
        print("|", end=" ")  # Abrir barra
        for num in fila:
            # Cada número se imprimirá con un ancho igual al del número más grande
            print(f"{num:>{max_digitos}}", end=" ")
        print("|")  # Cerrar barra

def multiplicar_matrices(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    columnas_matriz2 = len(matriz2[0])
    
    # Crear matriz resultado
    resultado = [[0 for _ in range(columnas_matriz2)] for _ in range(filas_matriz1)]
    
    # Multiplicar matrices (fila por columna)
    for i in range(filas_matriz1):
        for j in range(columnas_matriz2):
            for k in range(columnas_matriz1):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return resultado

# Ejemplo de uso
print("Llenado de la primera matriz")
while True:
    try:
        filas1 = int(input("Ingrese el número de filas para la matriz 1: "))
        columnas1 = int(input("Ingrese el número de columnas para la matriz 1: "))
        if filas1 <= 0 or columnas1 <= 0:
            print("Error: La cantidad de filas y columnas debe ser mayor que 0.")
        else:
            matriz1 = crear_matriz(filas1, columnas1)
            break
    except ValueError:
        print("Error: Debe ingresar un número entero positivo.")


print("\nLlenado de la segunda matriz")
while True:
    try:
        filas2 = columnas1  # Para que la multiplicación sea válida
        columnas2 = int(input("Ingrese el número de columnas para la matriz 2: "))
        if filas2 <= 0 or columnas2 <= 0:
            print("Error: La cantidad de filas y columnas debe ser mayor que 0.")
        else:
            matriz2 = crear_matriz(filas2, columnas2)
            break
    except ValueError:
        print("Error: Debe ingresar un número entero positivo.")

# Imprimir ambas matrices
print("\nMatriz 1:")
imprimir_matriz(matriz1)

print("\nMatriz 2:")
imprimir_matriz(matriz2)

# Multiplicar matrices
resultado = multiplicar_matrices(matriz1, matriz2)

# Imprimir resultado de la multiplicación
print("\nResultado de la multiplicación de matrices:")
imprimir_matriz(resultado)