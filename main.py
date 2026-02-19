from juego.personajes import Personaje
import interaccion.interaccion_usuario as interaccion_usuario
from juego.partida import partida

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

personaje_elegido = interaccion_usuario.elegir_personaje(TEXTO_SELECCION_PERSONAJE, TEXTO_ELEGIR_OPCION, ERROR_OPCION_PERSONAJE_INVALIDA, personajes )

interaccion_usuario.borrar_consola()

interaccion_usuario.mostrar_mensaje("")
interaccion_usuario.mostrar_mensaje(TITULO_COMBATE)

partida(TEXTO_ELEGIR_OPCION, ERROR_ATAQUE_DEFENSA, opcion_turno_valida, personaje_elegido, guardian)

interaccion_usuario.mostrar_mensaje("")
if personaje_elegido.vida <= 0:
    interaccion_usuario.mostrar_mensaje(TEXTO_DERROTA)
else:
    interaccion_usuario.mostrar_mensaje(TEXTO_VICTORIA)
interaccion_usuario.mostrar_mensaje("")