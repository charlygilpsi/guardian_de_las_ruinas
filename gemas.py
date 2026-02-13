class Gemas:

    def __init__(self):
        self.listaGemas = []


    def anadirGema(self, valor):
        self.listaGemas.append(valor)

    def quitarGema(self, valor):
        if valor in self.listaGemas:
            self.listaGemas.remove(valor) #existe discard() pero segun la ia "solo funciona con Conjuntos (set)"

    def valorMinimo(self):
        if self.listaGemas: # Si la lista NO está vacía
            return min(self.listaGemas)
        else:
            return "No hay gemas" #TODO: extraer langString
    
    def valorMaximo(self):
        if self.listaGemas: # Si la lista NO está vacía
            return max(self.listaGemas)
        else:
            return "No hay gemas" #TODO: extraer langString
    
    def valorPromedio(self):
        if self.listaGemas: # Si la lista NO está vacía
            return sum(self.listaGemas) / len(self.listaGemas)
        else:
            return "No hay gemas" #TODO: extraer langString