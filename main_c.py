from personajes import Personaje
from combate import turno, maquina_ataque
from utils import opcion_valida
import os

mago = Personaje("Mago", 80, 28, 8)
luchador = Personaje("Luchador", 120, 18, 14)
picaro = Personaje("Pícaro", 75, 24, 10)
barbaro = Personaje("Bárbaro", 140, 22, 12)
clerigo = Personaje("Clérigo", 130, 15, 18)
guardian = Personaje("Guardián", 200, 20, 15)

personajes = [mago, luchador, picaro, barbaro, clerigo]

# Banderas
fin_del_juego = False
opcion_personaje_valida = False
opcion_turno_valida = False
victoria = False

# Constantes
CANTIDAD_PERSONAJES = len(personajes)
TEXTO_ELEGIR_OPCION = "Introduzca aquí el número de la opción seleccionada: "
ERROR_OPCION_PERSONAJE_INVALIDA = f"ERROR: Introduzca un número entero entre 1 y {CANTIDAD_PERSONAJES}."
ERROR_ATAQUE_DEFENSA = "ERROR: Introduzca un 1 (atacar) o un 2 (defender)."

while not opcion_personaje_valida:
    print("")
    print("Seleccione un personaje: ")
    print("")
    for i, personaje in enumerate(personajes, start=1):
        print(f"{i}. {personaje.nombre}: {personaje.vida} puntos de vida, {personaje.ataque} puntos de ataque, {personaje.defensa} puntos de defensa")
        i = i + 1

    print("")
    opcion = input(TEXTO_ELEGIR_OPCION)

    if not opcion_valida(opcion, CANTIDAD_PERSONAJES):
        os.system("cls")
        print("")
        print(ERROR_OPCION_PERSONAJE_INVALIDA)
    else:
        opcion_personaje_valida = True

while not opcion_turno_valida:
    print("")
    print("COMBATE CONTRA EL GUARDIÁN")
    print("")
    print("Seleccione una acción: ")
    print("")
    print("1. Atacar")
    print("2. Defender")
    print("")
    opcion = input(TEXTO_ELEGIR_OPCION)
    
    if not opcion_valida(opcion, 1, 2):
        os.system("cls")
        print("")
        print(ERROR_ATAQUE_DEFENSA)
    else:
        accion_guardian = maquina_ataque()
    #    if opcion == "1":
            