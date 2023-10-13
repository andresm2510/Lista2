#ex16

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
        self.saude = max(0, self.saude - tempo_brincadeira)  
        sleep(1)
        print(f"{self.nome} brincou e sua saúde diminuiu.")

    def humor(self):
        humor = self.fome + self.saude
        print(f"Humor: {humor}")
        return humor

    def __str__(self):
        return f"Nome: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\nIdade: {self.idade}"

# Exemplo de uso
tamaguchi = Tamaguchi("Tama", 50, 80, 5)
while True:
    print("Escolha uma opção:")
    print("1 - Mostrar estado do Tamaguchi")
    print("2 - Alimentar")
    print("3 - Brincar")
    print("4 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        print(tamaguchi)
    elif opcao == "2":
        quantidade_comida = int(input("Quantidade de comida: "))
        tamaguchi.alimentar(quantidade_comida)
    elif opcao == "3":
        tempo_brincadeira = int(input("Tempo de brincadeira: "))
        tamaguchi.brincar(tempo_brincadeira)
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")
