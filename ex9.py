#ex9

class Ponto():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostra(self):
        print(f'({self.x},{self.y})')

    def pegar(self):
        return (self.x, self.y)


class Retangulo():

    def __init__ (self, h, l, ponto):
        self.h = h
        self.l = l
        self.ponto = Ponto(ponto) #ponto inferior esquerdo:
        
    def muda_valor(self, h, l, ponto):
        self.h = h
        self.l = l
        self.ponto = Ponto(ponto)

    def calcular_centro(self):

        x=  self.ponto.x + (self.l)/2
        y=  self.ponto.y + (self.h)/2

        return Ponto(x,y)