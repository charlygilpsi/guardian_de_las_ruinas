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

def turno(atacante, accion_atacante, defensor, accion_defensor):
    """
    Gestiona lo que sucede en cada turno en función de las acciones introducidas
    
    :param atacante: Personaje que ataca.
    :type atacante: dict
    :param accion_atacante: 1 si ataca y 0 si no.
    :type accion_atacante: int
    :param defensor: Personaje que defiende.
    :type defensor: dict
    :param accion_defensor: 0 si defiende y 1 si no.
    :type accion_defensor: int
    :return: Puntos de vida restantes del defensor.
    :rtype: int
    """
    if accion_atacante == 1:
        if accion_defensor == 1:
            return defensor.vida - (atacante.ataque - defensor.defensa)
        else:
            return defensor.vida - atacante.ataque
    else:
        return defensor.vida  


def maquina_ataque():
    """
    Decide aleatoriamente si la máquina ataca o defiende.

    :return: 1 ataca y 0 defiende.
    :rtype: int
    """
    return random.randint(0, 1)