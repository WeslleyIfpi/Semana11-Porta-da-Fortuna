from random import *

# Essa variável guarda o número de vezes que o jogo já foi jogado
tentativas = 0

score = 0

#Imprima as 3 portas e as instruçõs do jogo
print( '''
Porta da Fortuna!
========

Existe um super prêmio atrás de umas destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!

  _____   _____   _____
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |   o | |   o | |   o |
 |_____| |_____| |_____|
 ''')

#Repita enquanto a variáveç score for menor do que 3
while score < 3:

    #Soma 1 ao número de tentativas
    tentativas += 1

    print('\nTentativa', tentativas, ": Escolah uma porta (1, 2,ou 3):")

    #Pegue a porta escolhida e armazene como um número inetiro (int)
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)

    #Escolha aleatoriamente a porta que esconde o prêmio (entre 1 e 3)
    portaCerta = randint(1,3)

    #Mostre ao jogados qual porta ele escolheu e qual era a porta certa
    print('A posta escolhida fois a', portaEscolhida)
    print("A porta certa é a", portaCerta)

    #O jofgador danha se o número da porta escolhida e o da porta certa forem o mesmo
    if portaEscolhida == portaCerta:
        print('Parabéns!')
        score = score + 1
    else:
        print("Que peninha!")

    print("Sua pontuação atual é", score)

print("\n** Você conseguiu! Terminou o jogo em", tentativas, "Tentativas **")
