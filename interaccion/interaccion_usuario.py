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
        int: Número correspondiente a la acción elegia.
    """
    opcion_turno_valida = False

    while not opcion_turno_valida:
            print("")
            print("Seleccione una acción: ")
            print("")
            print("1. Atacar")
            print("2. Defender")
            print("")
            accion_personaje = input(texto_elegir_opcion)
            
            if not opcion_valida(accion_personaje, 2):
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