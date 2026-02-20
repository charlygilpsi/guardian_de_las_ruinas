from utils.utils import opcion_valida
import os

def elegir_personaje(texto_seleccion_personaje, texto_elegir_opcion, texto_opcion_personaje_invalida, array_personaje):
    """
    Bucle que se repite hasta que el usuario elija personaje.

    Args:
        texto_seleccion_personaje (str): Texto de selección de personaje.
        texto_elegir_opcion (str): Texto de elegir número de opción.
        texto_opcion_personaje_invalida (str): Texto error al elegir personaje.
        array_personaje (list): Array con objetos Personaje.

    Returns:
        Personaje: Objeto de la clase Personaje elegido por el usuario
    """
    opcion_personaje_valida = False

    while not opcion_personaje_valida:
        print("")
        print(texto_seleccion_personaje)
        print("")
        i = 1
        for personaje in array_personaje:
            print(f"{i}. {personaje.nombre}: {personaje.vida} puntos de vida, {personaje.ataque} puntos de ataque, {personaje.defensa} puntos de defensa")
            i = i + 1

        print("")
        opcion = input(texto_elegir_opcion)

        if not opcion_valida(opcion, len(array_personaje)):
            os.system("cls")
            print("")
            print(texto_opcion_personaje_invalida)
        else:
            opcion_personaje_valida = True
            return array_personaje[int(opcion) - 1]


def seleccionar_accion(texto_elegir_opcion, error_ataque_defensa, opcion_turno_valida): 
    """
    Bucle que se repite hasta que el usuario elige la acicón en el turno.

    Args:
        texto_elegir_opcion (str): Texto de introducir opción.
        error_ataque_defensa (str): Texto de error de input de entrada.
        opcion_turno_valida (bool): Bandera que cambia si la opción elegida es válida

    Returns:
        int: Número correspondiente a la acción elegida.
    """
    opcion_turno_valida = False

    while not opcion_turno_valida:
            print("")
            print("Seleccione una acción: ")
            print("")
            print("1. Atacar")
            print("2. Defender")
            print("3. Log del combate")
            print("4. Salir")
            print("")
            accion_personaje = input(texto_elegir_opcion)
            
            if not opcion_valida(accion_personaje, 4):
                os.system("cls")
                print("")
                print(error_ataque_defensa)

            else:
                opcion_turno_valida = True
                return int(accion_personaje)
            

def mostrar_mensaje(mensaje):
    """
    Muestra el mensaje por consola.

    Args:
        mensaje (str): Mensaje a mostrar.
    """   
    print(mensaje)
    
    
def borrar_consola():
    """
    Borrar lo que había en consola.
    """
    os.system("cls")
    
    
def rellenar_log(contador_turno, mensaje_turno_jugador, mensaje_turno_maquina, log):
    """
    Añade lo sucedido en cada turno en el log.

    Args:
        contador_turno (int): Contador de turnos.
        mensaje_turno_jugador (str): Descripción de lo sucedido en el turno del jugador.
        mensaje_turno_maquina (str): Descripción de lo sucedido en el turno de la máquina.
        log (list): Log donde se va guardando lo sucedido en cada turno.
    """
    contenido = f"Turno {contador_turno}\n\n{mensaje_turno_jugador}\n\n{mensaje_turno_maquina}\n\n"
    log.append(contenido)
    

def mostrar_log(log):
    """
    Imprime el log por pantalla

    Args:
        log (list): Array que contiene lo sucedido en cada turno.
        
    Returns:
        str: Devuelve lo sucedido en cada turno.
    """
    for turno in log:
        mostrar_mensaje(turno)
    
    mostrar_mensaje("")
    input("Pulse Intro para continuar...")