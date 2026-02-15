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

def imprimirClases():
    i = 1
    for clase in clases:
        print(f"{i}- Clase: {clase[0]}, vida: {clase[1]}, ataque: {clase[2]}, defensa{clase[3]}")
        i += 1

def claseValida(opcion):
    encontrada = False
    for clase in clases:
        if clase[0] == opcion:
            encontrada = True
    return encontrada

def getClase(opcion):
    if opcion.isdigit():   # devuelve la tupla correspondiente
        if 1 <= int(opcion) < len(clases):
            return clases[int(opcion)-1]
    
    for clase in clases:    # busca por el nombre de la clase y la devuelve
        if opcion == clase[0]:
            return clase    
    
    return False    # si no encuentra nada

#pedir calse al usuario
datos_pj = False
while not datos_pj:
    imprimirClases()
    seleccion_clase = input("Introduce la clase de tu PJ:_ ").capitalize()
    datos_pj = getClase(seleccion_clase)
    if datos_pj is not False:
        jugador = Personaje(datos_pj[0], datos_pj[1], datos_pj[2], datos_pj[3])
print(jugador.nombre)

enemigo = Personaje("Enemigo", 150, 50, 5)


#ejecucion del juego
turno_jugador = True
while jugador.vida > 0 or enemigo.vida > 0:

    accion_jugador = input("introduce la accion: atacar/defender").capitalize()
    if accion_jugador == "Atacar":
        atacar_jugador = True
    else:
        atacar_jugador = False
      
    accion_enemigo = combate.maquina_ataque()
    if accion_enemigo == 1:
        accion_enemigo = True
    else:
        accion_enemigo = False


    if turno_jugador:
        # (atacante, accion_atacante, defensor, accion_defensor
        print(combate.turno(jugador, atacar_jugador, enemigo, accion_enemigo))
    else:
        print(combate.turno(enemigo, accion_enemigo, jugador, atacar_jugador))
    
    turno_jugador = not turno_jugador