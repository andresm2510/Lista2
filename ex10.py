
class BombaDeCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valorLitro
        if litros_abastecidos <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros_abastecidos
            return f"Abastecidos {litros_abastecidos:.2f} litros de {self.tipoCombustivel}. Total a pagar: R$ {valor:.2f}"
        else:
            return "Quantidade insuficiente de combustível na bomba."

    def abastecerPorLitro(self, litros):
        valor_a_pagar = litros * self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            return f"Abastecidos {litros:.2f} litros de {self.tipoCombustivel}. Total a pagar: R$ {valor_a_pagar:.2f}"
        else:
            return "Quantidade insuficiente de combustível na bomba."

    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor

    def alterarCombustivel(self, novo_combustivel):
        self.tipoCombustivel = novo_combustivel

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade

#Exemplo
bomba = BombaDeCombustivel("Gasolina", 5.0, 1000.0)
print(bomba.abastecerPorValor(50))  
print(bomba.abastecerPorLitro(20))  
print(bomba.quantidadeCombustivel)  

bomba.alterarValor(5.5) 
bomba.alterarCombustivel("Etanol")  
bomba.alterarQuantidadeCombustivel(800)  
