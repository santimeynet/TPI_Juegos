import random  # Importa la biblioteca random para generar números aleatorios
import os  # Importa la biblioteca os para trabajar con archivos y rutas

def checker(integer, number_cad, rights): # Función checker para comparar el número ingresado con el número objetivo
    resultado = ""  # Almacena el resultado de la comparación
    for i in range(len(integer), 5):  # Completa con ceros a la izquierda si el número tiene menos de 5 cifras
        integer = "0" + integer
    for i in range(5):  # Itera sobre cada cifra para comparar
        if integer[i] == number_cad[i]:  # Si la cifra es correcta y está en la posición correcta
            resultado += "\033[42m" + integer[i]  # Pinta en verde
        else:
            resultado += "\033[41m" + integer[i]  # Pinta en rojo si la cifra es incorrecta
    return resultado + "\033[0;40m"  # Devuelve el resultado con códigos de color reset

def LoadUp(table, link):
    with open(link + "\\puntos.txt", "r", encoding="utf-8") as scores:  # Abre el archivo de puntajes para leer el historial
        lines = scores.read()
        if(len(lines) > 13):  # Si hay puntajes guardados
            for line in lines.splitlines():  # Carga cada línea de puntaje en la tabla
                table.append([line[:6], int(line[6:10]), int(line[10:14])])

def SaveUp(table, link):
    with open(link + "\\puntos.txt", "w") as scores:  # Guarda la tabla de puntajes en el archivo
        print("\nTabla de puntajes:\nJugador     Partidas    Partidas    Porcentaje")
        print("            Ganadas     Jugadas")
        for i in range(len(table)):
            line = table[i][0]
            line += " " * (13 - len(str(table[i][1]))) + str(table[i][1]) + " " * (13 - len(str(table[i][2]))) + str(table[i][2]) + " " * (13 - len(str(int(table[i][1] / table[i][2])))) + str(int(100 * table[i][1] / table[i][2])) + "%"
            print(line)
            scores.write(table[i][0])
            scores.write("0" * (4 - len(str(table[i][1]))) + str(table[i][1]))
            if(i < (len(table) - 1)):
                scores.write("0" * (4 - len(str(table[i][2]))) + str(table[i][2]) + "\n")
            else:
                scores.write("0" * (4 - len(str(table[i][2]))) + str(table[i][2]))
                
def main(): # Función principal
    table = []  # Tabla de puntajes
    list_aux = []  # Lista auxiliar para ordenar puntajes
    rights = [0, 0, 0, 0, 0]  # Lista para almacenar aciertos por posición
    number_cad = str(random.randrange(10000, 99999))  # Genera un número aleatorio de 5 cifras
    number = int(number_cad)  # Convierte el número a entero
    integer = 0  # Número ingresado por el usuario
    attemps = 7  # Número de intentos permitidos
    hint = ""  # Pista para el jugador
    link = os.path.dirname(__file__)  # Ruta del archivo actual
    band = True  # Bandera para verificar si el jugador ya está en la tabla
    LoadUp(table, link)
    print("Debe ingresar un número de 5 cifras. Si la cifra está en la ubicación correcta se pintará de verde, de lo contrario,") # Instrucciones para el jugador
    print("se pintará de rojo. Al lado de cada número saldrá una flecha, que indicará si el número a descubrir es menor ▼ o mayor ▲.")
    print("Contarás con 7 intentos")
    os.system("PAUSE")  # Pausa antes de iniciar
    os.system("cls")  # Limpia la pantalla
    while True:  # Bucle principal del juego
        cad = input("Ingrese un número: ")[:5]  # Lee el número del usuario
        for i in range(len(cad)):  # Verifica si solo contiene dígitos
            if(ord(cad[i]) < 48 or ord(cad[i]) > 57):
                cad = cad.replace(cad[i], " ")
        cad = cad.replace(" ", "")
        if (not len(cad)):
            cad = "0"
        integer = int(cad)  # Convierte el número ingresado a entero
        hint = checker(str(integer), number_cad, rights)  # Genera pista de colores
        if number < integer:
            hint += " ▼"  # Flecha si el número es mayor
        elif number > integer:
            hint += " ▲"  # Flecha si el número es menor
        print(hint)  # Muestra la pista y puntaje
        if number == integer or attemps == 0:  # Termina si acierta o se quedan sin intentos
            break
        attemps -= 1  # Resta intentos
    name = input("\nIngresa tu nombre para registrar tu puntuación:\nNombre: ")[:6].upper()  # Nombre máximo 6 caracteres
    name += " " * (6 - len(name))  # Completa con espacios para formato
    for i in range(len(table)):  # Busca si el jugador ya está en la tabla
        if(name == table[i][0]):
            table[i][2] += 1  # Incrementa partidas jugadas
            band = False
            if(attemps >= 0):  # Suma partidas ganadas si acertó
                table[i][1] += 1
    if(band):  # Si el jugador es nuevo, lo añade a la tabla
        table.append([name, 0, 1])
        if(attemps >= 0):  # Marca como ganada si acertó
            table[-1][2] += 1
    for i in range(len(table) - 1): # Ordena la tabla de puntajes
        aux = i
        for j in range(i + 1, len(table)):
            if(table[aux][1] < table[j][1]):
                aux = j
            elif(table[aux][1] == table[j][1] and table[aux][2] > table[j][2]):
                aux = j
        table[i], table[aux] = table[aux] , table[i]
    SaveUp(table, link)
    jd = int(input("¿Desea volver a jugar? SI = 1 // Menu principal = 2\n"))
    if jd == 1:
        main()
    else:
        os.system("cls")
        print("Volviendo al menu principal...")


if __name__ == "__main__":
    main()