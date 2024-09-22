# InicioAlgoritmo
# Función para agregar elementos a la lista
def Agregar_Elmnts():
    lista = []
    # Repite hasta obtener 20 números enteros
    while len(lista) < 10:
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

# Función del menú principal
def Menu():
    lista = []
    while True:
        # Muestra el menú principal al usuario
        print("\nMenú Principal:")
        print("1. Agregar 20 números a la lista")
        print("2. Mostrar la lista")
        print("3. Ordenar y mostrar la lista")
        print("4. Mostrar la longitud de la lista")
        print("5. Buscar un número en la lista")
        print("6. Salir")
        
        # Captura la opción seleccionada por el usuario
        opcion = input("Seleccione una opción (1 al 6): ")
        
        # Ejecuta la función correspondiente según la opción seleccionada
        if opcion == '1':
            lista = Agregar_Elmnts()
        elif opcion == '2':
            Mostrar_Lista(lista)
        elif opcion == '3':
            Ordenar_Lista(lista)
        elif opcion == '4':
            Mostrar_Longitud(lista)
        elif opcion == '5':
            Buscar_Elemento(lista)
        elif opcion == '6':
            print("Gracias por utilizar nuestro programa. Hasta la próxima")
            break
        else:
            print("Opción no válida, ingrese un número del 1 al 6")

# Inicia el programa llamando a la función del menú
Menu()
#FinAlgoritmo