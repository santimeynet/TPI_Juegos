import os
import random
import menu

# Funcion del juego.

def trivia():

    # Array de preguntas y respuestas.
    preguntas_respuestas = {
        "Deportes": [
            ("¿Cuántos balones de oro ganó Messi?. Responda con número.", "8"),
            ("¿Cómo se llama el actual corredor argentino de F1?", "Franco Colapinto"),
            ("¿El último equipo en ganar la Champions League fue?", "Real Madrid"),
            ("¿En que años la seleccion argentina ganó el mundial? El formato de respuesta tiene que ser ...., .... y ....", "1978, 1986 y 2022"),
            ("¿Cuánto vale un try en rugby sin su conversión?. Responda con número.", "5")
        ],
        "Ciencia": [
            ("¿Cuál es el nombre del elemento químico Hg?", "Mercurio"),
            ("¿Cómo se llama la capa que cubre a la tierra de los rayos UV?", "Capa de Ozono"),
            ("¿Qué pigmento les da a las planta el color verde?", "Clorofila"),
            ("¿Qué significa H2O?", "Agua"),
            ("¿Cuál es el animal más grande del mundo?", "Ballena Azul")
        ],
        "Entretenimiento": [
            ("¿Cómo se llamaba el bicho de ojos claros en el Señor De Los Anillos?", "Gollum"),
            ("¿Cómo se llama la serie que tiene como protagonista a Pepe Argento?", "Casados con Hijos"),
            ("¿Qué personaje de los X-MEN se cura rapidamente?", "Wolverine"),
            ("¿Cuál es el apellido de Rocky en las peliculas?", "Balboa"),
            ("¿Qué actor interpreta a Jack Dawson en Titanic?", "Leonardo DiCaprio")
        ],
        "Geografía": [
            ("¿Cuál es la capital de Canadá?", "Otawa"),
            ("¿En que ciudad estoy si voy a visitar la Estatua de la Libertad?", "Nueva York"),
            ("¿Cuántas maravillas del mundo existen?. Responda con número.", "7"),
            ("¿Cuál es el pais más grande del mundo?", "Rusia"),
            ("¿Cuántos continentes existen?. Responda con número.", "6")
        ],
        "Cultura General": [
            ("¿En que año termino la segunda guerra mundial?", "1945"),
            ("¿Qué dia se celebra la independencia en Argentina?", "9 de Julio"),
            ("¿Quién descubrió América?", "Cristobal Colon"),
            ("¿Cuál es el actual presidente de la Republica Argentina?", "Javier Milei"),
            ("¿Dónde nació Juana de Arco?", "Francia")
        ]
    }

    # Pedimos el nombre del jugador
    nombre = input(f"¡Ingrese su nombre y apellido para comenzar el juego!\n")

    print(f"Genial {nombre}, vamos a jugar a un preguntas y respuestas!")


    puntuacion = 0
    categorias = list(preguntas_respuestas.keys())
    random.shuffle(categorias)

    # Ciclo for para recorrer las categorias e imprimir cada una de las preguntas.

    for categoria in categorias:
        print(f"\nCategoría: {categoria}")
        preguntas = random.sample(preguntas_respuestas[categoria], 5)
        
        for pregunta, respuesta_correcta in preguntas:
            print(pregunta)
            respuesta_usuario = input("Tu respuesta: ")
            
            if respuesta_usuario.strip().lower() == respuesta_correcta.lower():
                print("¡Correcto!")
                puntuacion += 1
            else:
                print(f"Incorrecto. La respuesta correcta es: {respuesta_correcta}")
                
    print(f"\nJuego terminado. {nombre}, tu puntuación es: {puntuacion}/25")

    # Guardar la puntuación en un archivo
    ruta_archivo = os.path.join(os.path.dirname(__file__), "puntos.txt")
    with open(ruta_archivo, "a") as puntos:
        puntos.write(f"{nombre}: {puntuacion}/25\n")
    print("Tu puntuación ha sido guardada en 'puntos.txt'.")

    # Preguntamos si se quiere volver a jugar.
    jugar_nuevamente = int(input(f"¿Desea volver a jugar?. 1 = SI // ENTER para volver al menú principal.\n"))

    if jugar_nuevamente == 1:
        trivia()
    else:
        menu()

if __name__ == "__main__":
    trivia()


