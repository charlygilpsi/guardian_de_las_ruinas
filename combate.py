import random

def maquina_ataque():
    """
    Decide aleatoriamente si la máquina ataca o defiende.

    :return: 1 ataca y 0 defiende.
    :rtype: int
    """
    return random.randint(0, 1)


def turno(atacante, accion_atacante, defensor, accion_defensor):
    """
    Gestiona lo que sucede en cada turno en función de las acciones introducidas.
    
    :param atacante: Personaje que ataca.
    :type atacante: Personaje
    :param accion_atacante: 1 si ataca y 0 si no.
    :type accion_atacante: int
    :param defensor: Personaje que defiende.
    :type defensor: Personaje
    :param accion_defensor: 0 si defiende y 1 si no.
    :type accion_defensor: int
    :return: Mensaje descriptivo del turno.
    :rtype: str
    """

    if accion_atacante == 1:
        if accion_defensor == 0:
            daño = max(0, atacante.ataque - defensor.defensa)
            defensor.vida = defensor.vida - daño
            mensaje = (
                f"{atacante.nombre} ataca y causa {daño} puntos de daño. {defensor.nombre} tiene ahora {defensor.vida} puntos de vida."
            )
        else:
            defensor.vida = defensor.vida - atacante.ataque
            mensaje = (
                f"{atacante.nombre} ataca y causa {daño} puntos de daño. {defensor.nombre} tiene ahora {defensor.vida} puntos de vida."
            )
    else:
        mensaje = (
            f"{atacante.nombre} no ha atacado. {defensor.nombre} tiene {defensor.vida} puntos de vida."
        )

    return mensaje