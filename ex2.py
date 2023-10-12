#ex2

class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def mudaLado(self, lado):
        self.lado = lado
    
    def mostraLado(self):
        print(self.lado)

    def calculaArea(self):
        area = self.lado * self.lado
        print(area)