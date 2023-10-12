#ex3

class Retangulo:


    def __init__(self,ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudaLado(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mostraLado(self):
        print(self.ladoA)
        print(self.ladoB)

    def calculaArea(self):
        area = self.ladoA * self.ladoB
        print(area)
        return area

    def calculaPerimetro(self):
        perimetro = 2 * (self.ladoA + self.ladoB)
        print(perimetro)
        return perimetro