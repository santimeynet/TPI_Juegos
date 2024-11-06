import os

import random

def mayormenor():
    aleatorio =  random.randint(1, 100)
    puntaje = 0
    
    nombre =  input("Ingrese un nombre\n")

    while True:
        num = int(input("Ingrese el numero entre 1 y 100\n"))
        puntaje += 1
        if num == aleatorio:
            print("Felicidades adivinaste el numero!!")
            break
        elif num < aleatorio:
            print("El numero es mayor, intenta nuevamente")
        else:
            print("El numero es menor, intente nuevamente")
        ruta_archivo = os.path.join(os.path.dirname(_file_), "puntaje.txt")
    with open(ruta_archivo, "a") as puntos:
        puntos.write(f"{nombre}: {puntaje}\n")
    print("Tu puntuación ha sido guardada en 'puntaje.txt'.")
    ruta_archivo = os.path.join(os.path.dirname(_file_), "puntaje.txt")
    with open(ruta_archivo, "r") as archivo:
        for linea in archivo:
            nombre, puntaje = linea.strip().split(":") 
            print(f"Nombre: {nombre}, Intentos: {puntaje}")
    print("Fin del juego")
mayormenor()
