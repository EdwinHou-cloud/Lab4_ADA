def Pronunciar():
    
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

    while True:  # Bucle que repite hasta que se ingrese una entrada válida
        # Solicita al usuario que ingrese una letra o palabra
        entrada = input("Introduce una letra o una palabra: ").upper()
        
        # Si el usuario ingresa una letra (un solo carácter)
        if len(entrada) == 1:  # Es una letra
            # Verifica si la letra está en el diccionario
            if entrada in Alfabeto_Japones:
                print(f"La pronunciación en japonés de la letra {entrada} es {Alfabeto_Japones[entrada]}")
            else:
                print("Letra no reconocida.")
        else:  # Si el usuario ingresa una palabra (más de un carácter)
            pronunciacion = ""
            # Recorre cada letra de la palabra
            for letra in entrada:
                # Verifica si cada letra está en el diccionario
                if letra in Alfabeto_Japones:
                    pronunciacion += Alfabeto_Japones[letra] + " "
                else:
                    pronunciacion += letra + " "  # Si la letra no está, la deja igual
            # Muestra la pronunciación de la palabra
            print(f"La pronunciación en japonés de la palabra {entrada} es: {pronunciacion}")
            break  # Termina el bucle si la entrada es válida
    else:
        print("Entrada no válida. Solo se permiten letras. Inténtalo de nuevo.")

# Ejecuta la función pronunciar
Pronunciar()