from personajes import Personaje

#crear personaje
nombre_personaje = input("ingresa el nombre de tu personaje:_")
ataque_personaje = input("ingresa el ataque:_")
defensa_personaje = input("ingresa la defensa:_")
vida_personaje = input("ingresa la vida:_")

jugador = Personaje(nombre_personaje, vida_personaje, ataque_personaje, defensa_personaje)


enemigo = Personaje()