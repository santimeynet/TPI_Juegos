import os
import random


def kinggame():

    def guardar_datos(nombre, puntos):
        ruta_archivo = os.path.join(os.path.dirname(__file__), "datos.txt")
        with open(ruta_archivo, "a") as archivo:
            archivo.write(f"{nombre},{puntos}\n")
    
    def mostrar_datos():
        try:
            ruta_archivo = os.path.join(os.path.dirname(__file__), "datos.txt")
            with open(ruta_archivo, "r") as archivo:
                for linea in archivo:
                    nombre, puntos = linea.strip().split(",") 
                    print(f"Nombre: {nombre}, Puntos: {puntos}")
        except FileNotFoundError:
            print("El archivo no existe. Asegúrate de que se hayan guardado datos previamente.")

    
    economia=30
    pueblo=30
    ejercito=30
    
    eventos=[str()for i in range (15)]
    eventos [0]="Introducción de un sistema de salud universal financiado por una disminución en el gasto militar.\n\nAceptar: Mejora la salud pública, pero reduce el presupuesto militar.\nRechazar: Mantiene el presupuesto militar, pero limita la expansión de la salud pública."
    eventos [1]="Aumento del presupuesto militar para mejorar la seguridad nacional, lo que reduce fondos para servicios sociales.\n\nAceptar: Fortalece la seguridad nacional a expensas de otros sectores.\nRechazar: Mantiene los fondos en servicios sociales."
    eventos [2]="Implementación de un programa de bienestar social que redistribuye impuestos a las familias más necesitadas.\n\nAceptar: Mejora el bienestar social, pero afecta al presupuesto militar.\nRechazar: Preserva los fondos militares."
    eventos [3]="Tratado de libre comercio con un país vecino que reduce aranceles pero aumenta la competencia local.\n\nAceptar: Estimula la economía pero puede afectar a las industrias locales.\nRechazar: Protege la industria local, pero ralentiza el crecimiento económico."
    eventos [4]="Reducción del gasto en defensa para financiar la construcción de infraestructuras públicas.\n\nAceptar: Mejora infraestructuras a expensas de la seguridad.\nRechazar: Mantiene el gasto militar."
    eventos [5]="Reforma educativa que aumenta el gasto en educación, reduciendo el presupuesto militar.\n\nAceptar: Prioriza la educación sobre la defensa.\nRechazar: Mantiene el foco en el gasto militar."
    eventos [6]="Aumento de impuestos para financiar el desarrollo de nuevas tecnologías militares.\n\nAceptar: Moderniza el ejército, pero afecta a la economía.\nRechazar: Evita el aumento de impuestos, pero reduce la modernización."
    eventos [7]="Privatización de industrias estatales para mejorar la eficiencia económica, pero aumentando el desempleo.\n\nAceptar: Mejora la economía, pero genera desempleo.\nRechazar: Mantiene el control estatal y evita el desempleo."
    eventos [8]="Implementación de un programa de inmigración masiva para aumentar la mano de obra.\n\nAceptar: Aumenta la población y la economía, pero puede generar tensiones sociales.\nRechazar: Mantiene el equilibrio demográfico actual."
    eventos [9]="Participación en una alianza militar internacional que requiere un aumento del gasto en defensa.\nAceptar: Fortalece la defensa a nivel global, pero afecta la economía y la población.\nRechazar: Evita compromisos militares internacionales."
    eventos [10]="Reducción de los impuestos a las grandes empresas para estimular la inversión privada.\n\nAceptar: Fomenta la inversión privada, pero reduce ingresos fiscales.\nRechazar: Mantiene los impuestos, pero limita la inversión."
    eventos [11]="Se aprueba un aumento de las pensiones, financiado por un recorte en el presupuesto militar.\n\nAceptar: Mejora el bienestar de los pensionistas, pero afecta la defensa.\nRechazar: Preserva el presupuesto militar."
    eventos [12]="El ejercito solicita reclutamiento de miles de jóvenes.\n\nAceptar: Fortalece el ejército para la guerra, pero afecta la economía y la población.\nRechazar: Evita la guerra y el reclutamiento masivo."
    eventos [13]="Implementación de un plan de austeridad que reduce el gasto en defensa y en programas sociales.\n\nAceptar: Mejora la economía, pero reduce el apoyo social y militar.\nRechazar: Mantiene el gasto en defensa y programas sociales."
    eventos [14]="Nacionalización de sectores clave de la economía para aumentar el control estatal.\n\nAceptar: Aumenta el control estatal a costa de la economía.\nRechazar: Mantiene el sector privado y la economía estable."

    valores=[[0,10,-10,0,-10,10],[10,-10,-10,-10,10,10],[-10,0,10,0,-10,-10],[-10,10,0,0,-10,0],[10,-10,0,0,0,-10],[0,10,-10,0,-10,0],[0,-10,10,0,10,-10],[10,-10,0,-10,10,0],[10,10,-10,-10,-10,10],[0,0,10,0,0,0],[10,0,0,0,0,0],[0,10,-10,0,-10,10],[0,-10,10,0,10,-10],[20,-20,-20,-10,10,10],[10,0,-10,-10,0,0]]
    
    pf=0
    nom=input(str("Ingrese su nombre\n"))
    print("Como rey de un vasto y turbulento reino, cada decisión está en tus manos.Tus elecciones afectarán a tus economía, a tu gente y a las fuerzas del ejercito.\n ¿Lograrás mantener el equilibrio o caerá tu reino en el caos?")
    input("Presione cualquier tecla para iniciar\n")

    re = random.randint(0, len(eventos) - 1)    
    
    while economia > 0 and pueblo > 0 and ejercito > 0:
        print(eventos[re])
        decision=str(input()).lower()
        if decision == "aceptar" or "1":
            economia += valores[re][1]
            pueblo += valores[re][2]
            ejercito += valores[re][3]
        elif decision == "rechazar" or "2":
            economia += valores[re][4]
            pueblo += valores[re][5]
            ejercito += valores[re][6]
        else:
            print("Error decisión no valida")
            continue
        re = random.randint(0, len(eventos) - 1)
        pf = pf +1
        
    if economia <= 0:
        print("PERDSITE\n Tu economia llego a 0, el estado esta en banca rota.")
    elif pueblo <= 0:
        print("PERDISTE\n El pueblo se reveló contra el estado expulsandote del trono.")
    elif ejercito <= 0:
        print("PERDISTE\n El ejercito a tomado el mando mediente un golpe de estado.")

    guardar_datos(nom, pf)

    puntosFinal= mostrar_datos()

    vj=input("Ingrese 1 para volver a jugar o cualquier otro número para volver al menu. ")
    if vj == "1":
        kinggame()
    else:
        os.system("cls")
        print("Volviendo al menu principal...")


if __name__ == "__main__":
    kinggame()

