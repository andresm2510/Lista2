#ex13

class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_salario(self):
        return self.salario
    
    def get_nome(self):
        return self.nome
    
x= Funcionario('Joao', 1000)

print(x.get_nome())

print(x.get_salario())