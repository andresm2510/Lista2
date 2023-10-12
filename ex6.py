class Televisor:
    def __init__(self):
        self.volume = 10  
        self.canal = 1    

    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 10
            print(f"Volume aumentado para {self.volume}%")

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 10
            print(f"Volume diminuído para {self.volume}%")

    def mudar_canal(self, canal):
        if 1 <= canal <= 100:
            self.canal = canal
            print(f"Canal alterado para {self.canal}")
        else:
            print("Canal fora da faixa válida (1-100)")

    def mostrar_informacoes(self):
        print(f"Canal: {self.canal}")
        print(f"Volume: {self.volume}%")

# Exemplo de uso da classe Televisor:
tv = Televisor()

while True:
    print("\nControles do Televisor:")
    print("1 - Aumentar volume")
    print("2 - Diminuir volume")
    print("3 - Mudar de canal")
    print("4 - Mostrar informações da TV")
    print("0 - Desligar a TV")
    
    escolha = int(input("Escolha uma opção: "))
    
    if escolha == 1:
        tv.aumentar_volume()
    elif escolha == 2:
        tv.diminuir_volume()
    elif escolha == 3:
        novo_canal = int(input("Digite o número do canal desejado: "))
        tv.mudar_canal(novo_canal)
    elif escolha == 4:
        tv.mostrar_informacoes()
    elif escolha == 0:
        print("Desligando a TV. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
