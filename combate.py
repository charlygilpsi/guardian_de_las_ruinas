"""
El Sistema de Combate
•La Función de Turno: Crea una función llamada turno(atacante, accion_atacante, defensor, 
accion_defensor).
•Si el defensor elige defender, el daño será: ataque - defensa (mínimo 0).
•Si el defensor no se defiende, el daño será igual al ataque total.
•La función debe restar el daño a la vida del defensor y devolver el valor resultante.
•Simulación del Duelo: * El usuario elige la acción del aventurero (atacar o defender).
•El enemigo elige su acción de forma aleatoria.
•Muestra en consola el progreso de cada turno de forma clara (ej: "Lyria ataca y causa 
7 de daño. El Guardián tiene ahora 53 de vida").
"""

import random

def ataca_o_defiende():
    """
    Decide aleatoriamente si el enemigo ataca o defiende

    :return: True si ataca y False si defiende
    :rtype: bool
    """
    return random.randint(0, 1) == 1