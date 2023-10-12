class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} realizado. Novo saldo: R${self.saldo:.2f}')
        else:
            print('Valor de depósito inválido.')

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado. Novo saldo: R${self.saldo:.2f}')
        else:
            print('Saldo insuficiente ou valor de saque inválido.')

    def mostrarInformacoes(self):
        print(f'Número da Conta: {self.numero_conta}')
        print(f'Nome do Correntista: {self.nome_correntista}')
        print(f'Saldo: R${self.saldo:.2f}')

#Exemplo
conta1 = ContaCorrente("12345", "João")
conta1.mostrarInformacoes()

conta1.deposito(1000)
conta1.saque(500)
conta1.alterarNome("Maria")
conta1.mostrarInformacoes()
