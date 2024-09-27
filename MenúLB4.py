"""
Hou, Edwin	        8-1021-1916
Arosemena, Miguel	8-1016-2330
Corrales, Diego		8-1001-1890
Camaño, Edward		8-1010-515
Pino, Josué		    8-1012-688
"""

# InicioAlgoritmo
def presentacion():
    print("\n{:^70}".format("UNIVERSIDAD TECNOLÓGICA DE PANAMÁ"))
    print("{:^70}".format("FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES"))
    print("{:^70}".format("DEPARTAMENTO DE COMPUTACIÓN Y SIMULACIÓN DE SISTEMAS"))
    print("{:^70}".format("LABORATORIO #4"))
    print("{:^70}".format("Integrantes: Miguel Arosemana 8-1016-2330"))
    print("{:^78}".format("Edward Camaño 8-1010-515"))
    print("{:^80}".format("Diego Corrales 8-1001-1890"))
    print("{:^76}".format("Edwin Hou 8-1021-1916"))
    print("{:^76}".format("Josue Pino 8-1012-688"))

# Función para agregar elementos a la lista
def Agregar_Elmnts():
    lista = []
    # Repite hasta obtener 20 números enteros
    while len(lista) < 20:
        try:
            # Pide al usuario que ingrese un número entero positivo
            numero = int(input(f"Ingrese un número entero positivo ({len(lista)+1}/20): "))
            if numero < 0:  # Verificar que sea positivo
                print("Por favor, ingrese solo números positivos.")
            else:
                lista.append(numero)  # Agrega el número a la lista
        except ValueError:
            print("Por favor, ingrese un número.")
    return lista

# Función para mostrar la lista en una línea
def Mostrar_Lista(lista):
    print("Lista de números:", ' '.join(map(str, lista)))

# Función para ordenar y mostrar la lista
def Ordenar_Lista(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:", ' '.join(map(str, lista_ordenada)))

# Función para mostrar la cantidad de elementos en la lista
def Mostrar_Longitud(lista):
    print(f"La lista tiene {len(lista)} elementos.")

# Función para buscar un número en la lista
def Buscar_Elemento(lista):
    try:
        # Verifica si el número ingresado está o no en  la lista
        numero = int(input("Ingrese el número que desea buscar: "))
        if numero in lista:
            print(f"El número {numero} está en la lista.")
        else:
            print(f"El número {numero} no está en la lista.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

def procesar_matriz():
    """
    Esta función gestiona todo el proceso de creación, llenado, validación,
    multiplicación de matrices y finalmente la impresión del resultado.
    """
    # Función para crear una matriz a partir de la entrada del usuario
    def crear_matriz(filas, columnas):
        """
        Crea una matriz de tamaño filas x columnas con valores ingresados por el usuario.
        """
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                while True:
                    try:
                        valor = int(input(f"Ingrese el valor para la posición ({i}, {j}): "))
                        fila.append(valor)
                        break
                    except ValueError:
                        print("Error: Debe ingresar un número entero.")
            matriz.append(fila)
        return matriz

    # Función para imprimir una matriz con formato ajustado
    def imprimir_matriz(matriz):
        """
        Imprime una matriz con formato adecuado, ajustando el ancho de las columnas
        de acuerdo con el número más grande de la matriz.
        """
        max_digitos = max(len(str(num)) for fila in matriz for num in fila)
        for fila in matriz:
            print("|", end=" ")
            for num in fila:
                print(f"{num:>{max_digitos}}", end=" ")
            print("|")
    
    # Función para multiplicar dos matrices
    def multiplicar_matrices(matriz1, matriz2):
        """
        Multiplica dos matrices y retorna la matriz resultado.
        """
        filas_matriz1 = len(matriz1)
        columnas_matriz1 = len(matriz1[0])
        columnas_matriz2 = len(matriz2[0])

        # Crear matriz resultado (inicialmente llena de ceros)
        resultado = [[0 for _ in range(columnas_matriz2)] for _ in range(filas_matriz1)]

        # Multiplicar matrices (fila por columna)
        for i in range(filas_matriz1):
            for j in range(columnas_matriz2):
                for k in range(columnas_matriz1):
                    resultado[i][j] += matriz1[i][k] * matriz2[k][j]
        return resultado

    # Proceso principal de la función
    try:
        # Solicitar dimensiones de la primera matriz
        print("Llenado de la primera matriz")
        filas1 = int(input("Ingrese el número de filas para la matriz 1: "))
        columnas1 = int(input("Ingrese el número de columnas para la matriz 1: "))
        if filas1 <= 0 or columnas1 <= 0:
            print("Error: La cantidad de filas y columnas debe ser mayor que 0.")
            return  # Salir de la función si los datos no son válidos
        
        # Crear la primera matriz
        matriz1 = crear_matriz(filas1, columnas1)

        # Solicitar dimensiones de la segunda matriz
        print("\nLlenado de la segunda matriz")
        filas2 = columnas1  # Para que la multiplicación sea válida, las filas de la segunda matriz deben coincidir con las columnas de la primera
        columnas2 = int(input("Ingrese el número de columnas para la matriz 2: "))
        if columnas2 <= 0:
            print("Error: La cantidad de columnas debe ser mayor que 0.")
            return  # Salir de la función si los datos no son válidos
        
        # Crear la segunda matriz
        matriz2 = crear_matriz(filas2, columnas2)

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

    except ValueError:
        # Manejo de errores en caso de entrada inválida
        print("Error: Debe ingresar un número entero válido.")
    except IndexError:
        # Manejo de errores si las dimensiones de las matrices no permiten la multiplicación
        print("Error: Las dimensiones de las matrices no son compatibles para la multiplicación.")
        
# Función que recibe una letra o palabra del usuario y devuelve la pronunciación en japonés
def pronunciar():
    # Diccionario que contiene las letras del alfabeto y su pronunciación en japonés
    Alfabeto_Japones = {
        'A': 'ka', 'B': 'tu', 'C': 'mi', 'D': 'te',
        'E': 'ku', 'F': 'lu', 'G': 'gi', 'H': 'ri',
        'I': 'ki', 'J': 'zu', 'K': 'me', 'L': 'ta',
        'M': 'rin', 'N': 'to', 'O': 'mo', 'P': 'no',
        'Q': 'ke', 'R': 'shi', 'S': 'ari', 'T': 'chi',
        'U': 'do', 'V': 'ru', 'X': 'na', 'W': 'mei',
        'Y': 'fu', 'Z': 'ra'
    }

    # Solicita al usuario que ingrese una letra o palabra
    entrada = input("Introduce una letra o una palabra: ").upper()

    # Verifica si la entrada solo contiene caracteres alfabéticos
    if entrada.isalpha():  
        # Si el usuario ingresa una letra (un solo carácter)
        if len(entrada) == 1:
            if entrada in Alfabeto_Japones:
                # Imprime la pronunciación de la letra
                print(f"La pronunciación en japonés de la letra {entrada} es {Alfabeto_Japones[entrada]}")
            else:
                print("Letra no reconocida.")
        else:
            pronunciacion = ""
            # Recorre cada letra de la palabra para obtener su pronunciación
            for letra in entrada:
                pronunciacion += Alfabeto_Japones.get(letra, letra) + " "
            # Imprime la pronunciación de la palabra completa
            print(f"La pronunciación en japonés de la palabra {entrada} es: {pronunciacion}")
    else:
        print("Entrada no válida. Solo se permiten letras.")

# Función que muestra el menú principal y gestiona las opciones seleccionadas por el usuario
def menu():
    lista = []
    """
    Esta función muestra el menú principal del programa,
    permitiendo al usuario seleccionar entre multiplicar matrices,
    obtener pronunciaciones en japonés, ver la presentación del programa o salir.
    """
    while True:
        
        # Mostrar opciones del menú
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Presentación")
        print("2. Gestionar lista")
        print("3. Multiplicación de matrices")
        print("4. Pronunciación de letras/palabras en japonés")
        print("5. Salir")

        try:
            # Solicita al usuario seleccionar una opción
            opcion = input("Seleccione una opción del 1 al 4: ")

            # Gestiona las opciones del menú
            if opcion == "1":
                presentacion()
            elif opcion == "2":
                print("\nSeleccione una opción para la lista: ")
                print("A. Agregar 20 números a la lista")
                print("B. Mostrar la lista")
                print("C. Ordenar y mostrar la lista")
                print("D. Mostrar la longitud de la lista")
                print("E. Buscar un número en la lista")
                opcionQ = input("Seleccione una opción (A a E): ")
                if opcionQ == 'A'or opcionQ == 'a':
                    lista = Agregar_Elmnts()
                    
                elif opcionQ == 'B' or opcionQ == 'b':
                    if lista:  #Verifica si la lista esta vacia
                        Mostrar_Lista(lista)
                    else:
                        print("No hay elementos en la lista. Agregue algunos números primero.")
                elif opcionQ == 'C' or opcionQ == 'c':
                    Ordenar_Lista(lista)
                elif opcionQ == 'D' or opcionQ == 'd':
                    Mostrar_Longitud(lista)
                elif opcionQ == 'E' or opcionQ == 'e':
                    Buscar_Elemento(lista)
                    
            elif opcion == "3":
                procesar_matriz()  # Llama a la función de multiplicación de matrices

            elif opcion == "4":
                pronunciar()  # Llama a la función de pronunciación en japonés

            elif opcion == "5":
                # Opción para salir del programa
                print("Gracias por utilizar nuestro programa.")
                break

            else:
                # Mensaje de error si la opción seleccionada es inválida
                print("Opción no válida, por favor ingrese un número válido (1-4).")
        except ValueError:
                # Maneja errores si el usuario ingresa un valor no numérico
                print("Error: Por favor, ingrese un número válido.")

# Inicia el programa llamando a la función del menú
menu() 
# FinAlgoritmo