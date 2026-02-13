from personajes import Personaje
import combate


#personaje: nombre, vida, ataque, defensa
clases = [
    ["Guerrero", 100, 50, 50],
    ["Arquero", 50, 70, 30],
    ["Mago", 50, 150, 10],
    ["Picaro", 50, 50, 50],
    ["Paladin", 150, 40, 60]
]

i = 1
for clase in clases:
    print(f"{i}- Clase: {clase[0]}, vida: {clase[1]}, ataque: {clase[2]}, defensa{clase[3]}")
    i += 1


#pedir calse al usuario
datos_pj = None
while datos_pj is None:
    seleccion_clase = input("Introduce la clase de tu PJ:_").capitalize()
    for clase in clases:
        if clase[0] == seleccion_clase:
            datos_pj = clase
            break  # Detenemos la búsqueda al encontrarlo
        else:
            print("Clase no encontrada")
jugador = Personaje(datos_pj[0], datos_pj[1], datos_pj[2], datos_pj[3])


enemigo = Personaje("Enemigo", 150, 50, 5)


#ejecucion del juego
turno_jugador = True
while jugador.vida > 0 or enemigo.vida > 0:
    accion_jugador = input("introduce la accion: atacar/defender")
    accion_enemigo = combate.maquina_ataque()


    if turno_jugador:
        # (atacante, accion_atacante, defensor, accion_defensor
        combate.turno(jugador, accion_jugador, enemigo, accion_enemigo)
    else:
        combate.turno(enemigo, accion_enemigo, jugador, accion_jugador)
    
    turno_jugador = not turno_jugador