import interaccion.interaccion_usuario as interaccion_usuario
import juego.combate as combate

def partida(texto_elegir_opcion, error_ataque_defensa, opcion_turno_valida, personaje_elegido, guardian, contador_turno, log):
    """
    Ejecuta la partida hasta que el Guardián o el Jugador son derrotados

    Args:
        texto_elegir_opcion (str): Texto para elegir opciones.
        error_ataque_defensa (str): Texto de error de input de entrada.
        opcion_turno_valida (bool): Bandera para terminar el bucle si los inputs son válidos.
        personaje_elegido (Personaje): Objeto de la clase Personaje que representa la elección del usuario.
        guardian (Personaje): Objeto de la clase Persoanje que representa al Guardián.
        contador_turno (int): Número de turno.
        log (list): Array que contiene lo sucedido en cada turno.
        
        Returns:
            bool: Devuelve True si el usuario finaliza el programa y False si el programa termina normalmente.
    """
    fin_del_juego = False
    
    while not fin_del_juego:
        accion_personaje = interaccion_usuario.seleccionar_accion(texto_elegir_opcion, error_ataque_defensa, opcion_turno_valida)
        if accion_personaje == 3:
            interaccion_usuario.borrar_consola()
            interaccion_usuario.mostrar_log(log)
            interaccion_usuario.borrar_consola()
            continue
        elif accion_personaje == 4:
            interaccion_usuario.borrar_consola()
            interaccion_usuario.mostrar_mensaje("")
            interaccion_usuario.mostrar_mensaje("FIN DE PROGRAMA")
            interaccion_usuario.mostrar_mensaje("")
            return True
        
        contador_turno = contador_turno + 1
        opcion_turno_valida = False
        interaccion_usuario.borrar_consola()
        accion_guardian = combate.maquina_ataque()
        mensaje_turno_jugador = combate.turno(personaje_elegido, accion_personaje, guardian, accion_guardian)
        print("")
        interaccion_usuario.mostrar_mensaje(mensaje_turno_jugador)
        
        if guardian.vida <= 0:
            fin_del_juego = True
            continue

        mensaje_turno_maquina = combate.turno(guardian, accion_guardian, personaje_elegido, int(accion_personaje))
        print("")
        interaccion_usuario.mostrar_mensaje(mensaje_turno_maquina)
        interaccion_usuario.rellenar_log(contador_turno, mensaje_turno_jugador, mensaje_turno_maquina, log)

        if personaje_elegido.vida <= 0:
            fin_del_juego = True
            continue
        
    return False