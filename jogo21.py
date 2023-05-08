from random import *

print('''Vinte e um!
=============
Tente fazer exatamente 21 pontos!''') 

pontuacao = 0

while True:
    numero = randint(1,10)
    pontuacao += numero

    print(f"Seu proximo número é {numero}")
    print(f'Sua pontuação agora é {pontuacao}')
    continuar = input('\nGostaria de somar mais um número (s/n)\n').lower()
    
    if continuar == 'n': break

print(f'Sua pontuação final é {pontuacao}')
if pontuacao == 21:
    print('VOCÊ VENCEU!!')
else:
    print('Que pena!!')