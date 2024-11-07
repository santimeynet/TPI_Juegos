import Trivia.juego
import KingGame.kinggame
import MayorMenor.MayorMenor

def menu():
    print("******************************")
    print("¡Bienvenido al menu de juegos!")
    print("*******************************")
    print("1. ¡King Game!")
    print("2. ¡Mayor o Menor!")
    print("3. ¡Triviador!")
    print("4. ¡Juego!")
    print("*******************************")

    juego = int(input("¡Ingrese el numero del juego que desea iniciar!\n"))


    if juego == 1:
        KingGame.kinggame.kinggame()
    elif juego == 2:
        MayorMenor.MayorMenor.mayormenor()
    elif juego == 3:
        Trivia.juego.trivia()
    else:
        print("Ingrese un numero valido")

menu()