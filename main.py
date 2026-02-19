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
fin_del_juego = False

# Constantes
CANTIDAD_PERSONAJES = len(personajes)
TEXTO_ELEGIR_OPCION = "Introduzca aquí el número de la opción seleccionada: "
TEXTO_SELECCION_PERSONAJE = "Seleccione un personaje: "
TEXTO_VICTORIA = "¡Enhorabuena, has derrotado al Guardián!"
TEXTO_DERROTA = "Lástima, el Guardián te ha vencido, vuelve a intentarlo."
TITULO_COMBATE = "COMBATE CONTRA EL GUARDIÁN"
ERROR_OPCION_PERSONAJE_INVALIDA = f"ERROR: Introduzca un número entero entre 1 y {CANTIDAD_PERSONAJES}."
ERROR_ATAQUE_DEFENSA = "ERROR: Introduzca un 1 (atacar) o un 2 (defender)."

while not opcion_personaje_valida:
    print("")
    print(TEXTO_SELECCION_PERSONAJE)
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
        personaje_elegido = personajes[int(opcion) - 1]

os.system("cls")
print("")
print(TITULO_COMBATE)

while not fin_del_juego:
    while not opcion_turno_valida:
        print("")
        print("Seleccione una acción: ")
        print("")
        print("1. Atacar")
        print("2. Defender")
        print("")
        accion_personaje = input(TEXTO_ELEGIR_OPCION)
        
        if not opcion_valida(accion_personaje, 2):
            os.system("cls")
            print("")
            print(ERROR_ATAQUE_DEFENSA)

        else:
            opcion_turno_valida = True

    opcion_turno_valida = False
    os.system("cls")
    accion_guardian = maquina_ataque()
    mensaje_turno_jugador = turno(personaje_elegido, int(accion_personaje), guardian, accion_guardian)
    print("")
    print(mensaje_turno_jugador)

    if guardian.vida <= 0:
        fin_del_juego = True
        continue

    mensaje_turno_maquina = turno(guardian, accion_guardian, personaje_elegido, int(accion_personaje))
    print("")
    print(mensaje_turno_maquina)

    if personaje_elegido.vida <= 0:
        fin_del_juego = True
        continue

print("")
if personaje_elegido.vida <= 0:
    print(TEXTO_DERROTA)
else:
    print(TEXTO_VICTORIA)
print("")