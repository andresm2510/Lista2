#ex12

class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxaJuros = taxa_juros

    def adicioneJuros(self):
        juros = self.saldo * (self.taxaJuros / 100)
        self.saldo += juros

    def mostrarSaldo(self):
        print(f'Saldo: R${self.saldo:.2f}')


conta_poupanca = ContaInvestimento(1000.0, 10.0)


for _ in range(5):
    conta_poupanca.adicioneJuros()


conta_poupanca.mostrarSaldo()
