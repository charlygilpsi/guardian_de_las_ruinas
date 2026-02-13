from personajes import Personaje
from utils import opcion_valida
import os

mago = Personaje("Mago", 80, 28, 8)
luchador = Personaje("Luchador", 120, 18, 14)
picaro = Personaje("Pícaro", 75, 24, 10)
barbaro = Personaje("Bárbaro", 140, 22, 12)
clerigo = Personaje("Clérigo", 130, 15, 18)
guardian = Personaje("Guardián", 200, 20, 15)

personajes = [mago, luchador, picaro, barbaro, clerigo]

# Banderas para bucles
fin_del_juego = False
opcion_personaje_valida = False
opcion_turno_valida = False

# Constantes
CANTIDAD_PERSONAJES = len(personajes)
ERROR_OPCION_INVALIDA = f"ERROR: Introduzca un número entero entre 1 y {CANTIDAD_PERSONAJES}."

while not opcion_personaje_valida:
    print("")
    print("Seleccione un personaje: ")
    print("")
    for i, personaje in enumerate(personajes, start=1):
        print(f"{i}. {personaje.nombre}: {personaje.vida} puntos de vida, {personaje.ataque} puntos de ataque, {personaje.defensa} puntos de defensa")
        i = i + 1

    print("")
    opcion = input("Introduzca aquí el número del personaje: ")

    if not opcion_valida(opcion, CANTIDAD_PERSONAJES):
        os.system("cls")
        print("")
        print(ERROR_OPCION_INVALIDA)
    else:
        opcion_personaje_valida = True

