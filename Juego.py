
import random

# Contador para el marcador del juego
victorias = 0
derrotas = 0
empates = 0

print ("\nBienvenido al juego de piedra, papel o tijera")

# Opciones que puede seleccionar el juego
opciones = ["PIEDRA", "PAPEL", "TIJERA"]

#Un bucle que se repite hasta que el usuario quiera salir
Jugando = True
while Jugando:
    print ("\n---Nueva partida---") # usamos "\n" para hacer un salto de linea
    print ("1) Piedra")
    print ("2) Papel")
    print ("3) Tijera")
    print ("4) Salir")

    eleccion_usuario = input("Elige una opcion (1, 2, 3, 4): ")

    if eleccion_usuario == "4":  #if revisa si el usuario quiere salir
        print ("\nBuenas partidas! Hasta la proxima")
        Jugando = False

    elif eleccion_usuario in ["1", "2", "3"]:  #if revisa si el usuario eligio una opcion valida e in las opciones
        if eleccion_usuario == "1":
            jugada_usuario = "PIEDRA"
        elif eleccion_usuario == "2":
            jugada_usuario = "PAPEL"
        elif eleccion_usuario == "3":
            jugada_usuario = "TIJERA"

        jugada_pc = random.choice(opciones) # esta funcion elige un numero aleatorio entre las opciones dadas inialmente

        # Imprime la eleccion del usuario y la computadora
        print("\nTus elegiste:", jugada_usuario)
        print("\nLa computadora eligio:", jugada_pc)

    #Logica para evaluar las reglas del juego
        if jugada_usuario == jugada_pc:
           print("\nEs un empate!")
           empates = empates + 1

        elif (jugada_usuario == "TIJERA" and jugada_pc == "PAPEL") or \
             (jugada_usuario == "PAPEL" and jugada_pc == "PIEDRA") or \
            (jugada_usuario == "PIEDRA" and jugada_pc == "TIJERA"):
            print("\nGanaste esta ronda!")
            victorias = victorias + 1

        else:
            print("\nPerdiste esta ronda!")
            derrotas = derrotas + 1

    #Se muestra el marcador del juego
        print("\n---Marcador acumulado---")
        print("Victorias:", victorias)
        print("Derrotas:", derrotas)
        print("Empates:", empates)

        while True:
            respuesta = input("\n¿Deseas jugar otra ronda? (si/no): ").strip().lower() #strip y lower nos ayuda a eliminar espacios en blanco y mayusculas y minusculas
            if respuesta in ["si", "sí"]:
                break  # Sale de este pequeño bucle y continúa el juego
            elif respuesta == "no":
                print("\nGracias por jugar! Resumen final:")
                print("Victorias:", victorias,)
                print("Derrotas:", derrotas,)
                print("Empates:", empates)
                Jugando = False  # Detiene el juego completo
                break  # Sale del pequeño bucle
            else:
                print("Entrada invalida. Por favor responde únicamente 'si' o 'no'.")

    else:
        print("\nOpcion invalida. Por favor, elige un numero del 1 al 4.") #si el usuario eligio una opcion invalida    

        