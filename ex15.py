#ex15

from time import sleep

class Tamaguchi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alterarFome(self, nova_fome):
        self.fome = nova_fome

    def alterarSaude(self, nova_saude):
        self.saude = nova_saude

    def alterarIdade(self, nova_idade):
        self.idade = nova_idade

    def mostrarNome(self):
        print(f"Nome: {self.nome}")

    def mostrarFome(self):
        print(f"Fome: {self.fome}")

    def mostrarSaude(self):
        print(f"Saúde: {self.saude}")

    def mostrarIdade(self):
        print(f"Idade: {self.idade}")

    def alimentar(self, quantidade_comida):
        self.fome = max(0, self.fome - quantidade_comida)  
        sleep(1)
        print(f"{self.nome} foi alimentado e sua fome diminuiu.")

    def brincar(self, tempo_brincadeira):
        self.saude = max(100, self.saude - tempo_brincadeira)  
        sleep(1)
        print(f"{self.nome} brincou e sua saúde aumentou.")

    def humor(self):
        humor = self.fome + self.saude
        print(f"Humor: {humor}")
        return humor

#Exemplo
tamaguchi = Tamaguchi("Tama", 50, 80, 5)
tamaguchi.mostrarNome()
tamaguchi.mostrarFome()
tamaguchi.mostrarSaude()
tamaguchi.mostrarIdade()

tamaguchi.alimentar(20)
tamaguchi.brincar(15)

tamaguchi.mostrarFome()
tamaguchi.mostrarSaude()
tamaguchi.humor()
