#ex14

class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_salario(self):
        return self.salario
    
    def get_nome(self):
        return self.nome

    def aumentarSalario(self, porcentagem):
        x= (self.salario * porcentagem)/100
        self.salario += x
        return self.salario
    

x= Funcionario('Joao', 1000)

print(x.get_nome())

print(x.get_salario())

x.aumentarSalario(10)

print(x.get_salario())