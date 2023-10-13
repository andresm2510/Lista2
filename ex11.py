#ex11

class Carro:
    def __init__(self, consumo, qntdCombustivel):
        self.consumo = consumo
        self.qntdCombustivel = 0

    def adicionarGasolina(self, qntdCombustivel):
        self.qntdCombustivel = qntdCombustivel

    def obterGasolina(self):
        return self.qntdCombustivel
    
    def andar(self, distancia):

        if self.qntdCombustivel > 0:
            self.qntdCombustivel = self.qntdCombustivel - (distancia/self.consumo)
        else:
            print("Sem combustível!")

#Exemplo

fusquinha=Carro(15, 0)

x = int(input("Quantos litros de combustível deseja adicionar? "))

fusquinha.adicionarGasolina(x)
a=fusquinha.obterGasolina()

print(a, "\n")

y = int(input("Quantos quilômetros deseja andar? "))
fusquinha.andar(y)

b=fusquinha.obterGasolina()

print(b)