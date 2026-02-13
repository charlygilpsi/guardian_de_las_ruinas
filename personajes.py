class Personaje:

    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self):
        return self.ataque
    
    def defender(self):
        return self.defensa
    
    def setVida(self, value):
        self.vida = value