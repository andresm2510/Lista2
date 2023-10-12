#ex3

import ex3Classe 
'''
lados = float(input("Quais as medidas do local?|(separados por espaço)"))
lados = lados.split()

if len(lados) != 2:
    print("ERRO: Digite apenas dois valores")
    exit()

elif len(lados) == 2:
    global X
    global Y

    X = float(lados[0])
    Y = float(lados[1])
'''

X = float(input("Qual a medida do primeiro lado?"))
Y = float(input("Qual a medida do segundo lado?"))
ex3Classe.Retangulo(X,Y)


local = ex3Classe.Retangulo(X,Y)

a= ex3Classe.calculaArea()

b= ex3Classe.calculaPerimetro()

print("O local necessita de ", a, "m² de piso e ", b, "m de rodapé.")