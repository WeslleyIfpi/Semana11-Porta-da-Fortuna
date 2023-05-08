from random import *

#O usuário muda esta variável para terminar o jogo
jogando = True

score = 0

#imprima as 3 portas e as instruções do jogo
print('''
Porta da Fortuna!
========

Existe um super prêmio atrás de ma destas 3 posrtas!
Adivinhe qual é a posta certa para ganhar o prêmio!
  _____   _____   _____
 |     | |     | |     |
 | [1] | | [2] | | [3] |
 |   o | |   o | |   o |
 |_____| |_____| |_____|
 ''')

#repetir, equanto a variável 'jogando' estiver com valro 'True' (verdadeiro)
while jogando == True:

    print("\nEscolha uma porta (1, 2 ou 3):")

    #pegue a porta escolhida e a armazene como um número inteiro (int)
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)

    # Escolha aleatoriamente a porta que esconte o prêmio (entre 1 e 3)
    portaCerta = randint(1,3)

    # Mostre ao jogados qual porta ele escolheu e qual era a porta certa
    ("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)

    # O jogador ganha se o número da porta escolhida e o da porta certa forem o mesmo
    if portaEscolhida == portaCerta:
        print("Parabéns!")
        score += 1
    else:
        print("Que peninha!")
        score = 0

    print(f"Total de acertos: {score}")

    #Pergunte ao jogador se ele quer continuar jogando
    print("\nVocê quer jogar de novo? (s/n)")
    resposta = input().lower()

    #Terimina o jogo se o jogador digita 'n'
    if resposta ==  'n' or resposta == 'nao':
        jogando == False

print("Obrigado por jogar.")
print("Sua pontuação final é de", score)