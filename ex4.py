class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(anos)

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, anos):
        if self.idade < 21:
            self.altura += anos * 0.5

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} cm")

#Exemplo
pessoa1 = Pessoa("João", 18, 70, 170)
pessoa1.mostrar_informacoes()

pessoa1.envelhecer(2)
pessoa1.engordar(5)
pessoa1.emagrecer(2)
pessoa1.mostrar_informacoes()

pessoa1.envelhecer(5)
pessoa1.mostrar_informacoes()
