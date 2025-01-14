from importlib import import_module


import random

jogador = ''
numero = 0
sorteado = random.randint(1,10)
tentativas = 5
aux = 1

jogador = input("Digite seu nome:")
while aux<=tentativas:
    numero=int(input("Digite seu chute de 1 a 10\n"))
    if numero<sorteado:
        print("Seu chute é menor que o sorteado")
        print("Tentativa %d de %d" % (aux, tentativas))
    elif numero>sorteado:
        print("Se chute é maior que o sorteado")
        print("Tentativa %d de %d" % (aux, tentativas))
    else:
        print("PARABENS %s!! VC ACERTOU O NUMERO SORTEADO" % (jogador))
        break
    aux=aux+1
print("Numero sorteado era: %d" % (sorteado))
print("Fim de jogo")