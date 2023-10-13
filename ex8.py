#ex8

class macaco():
    def __init__(self, nome, bucho):
        self.nome = nome
        self.bucho = bucho

    def comer(self, comida):
        self.bucho.append(comida)

    def verBucho(self):
        return self.bucho

    def digerir(self):
        self.bucho = []

    def __str__(self):
        return "Nome: " + self.nome + "\nBucho: " + str(self.bucho)