from time import sleep
import random

class Bichinho:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 100)
        self.tedio = random.randint(0, 100)

    def alimentar(self):
        self.fome = max(0, self.fome - 10)
        print(f"{self.nome} foi alimentado e sua fome diminuiu.")

    def brincar(self):
        self.tedio = max(0, self.tedio - 10)
        print(f"{self.nome} brincou e seu tédio diminuiu.")

    def humor(self):
        humor = self.fome + self.tedio
        print(f"{self.nome} - Fome: {self.fome} | Tédio: {self.tedio} | Humor: {humor}")

class FazendaBichinhos:
    def __init__(self):
        self.bichinhos = []

    def adicionar_bichinho(self, nome):
        bichinho = Bichinho(nome)
        self.bichinhos.append(bichinho)
        print(f"{nome} foi adicionado à fazenda.")

    def alimentar_todos(self):
        for bichinho in self.bichinhos:
            bichinho.alimentar()

    def brincar_todos(self):
        for bichinho in self.bichinhos:
            bichinho.brincar()

    def ouvir_todos(self):
        for bichinho in self.bichinhos:
            bichinho.humor()

# Exemplo de uso
fazenda = FazendaBichinhos()

# Adicione alguns bichinhos à fazenda
fazenda.adicionar_bichinho("Bichinho1")
fazenda.adicionar_bichinho("Bichinho2")

while True:
    print("Escolha uma opção:")
    print("1 - Alimentar todos os bichinhos")
    print("2 - Brincar com todos os bichinhos")
    print("3 - Ouvir todos os bichinhos")
    print("4 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        fazenda.alimentar_todos()
    elif opcao == "2":
        fazenda.brincar_todos()
    elif opcao == "3":
        fazenda.ouvir_todos()
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")
