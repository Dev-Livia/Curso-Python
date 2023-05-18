#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
print('=-=' * 20)
print('Vou pensar em um número de 0,5, Tente advinhar...')
print('=-=' * 20)
Jogador = int(input('Digite um número: '))
Computador = randint(0,5)
print('O computador escolheu o número {} e o jogador o número {}'.format(Computador, Jogador))
if Jogador > Computador:
    print('O Jogador VENCEU !!')
    if Computador == Jogador:
        print('EMPATE')
else:
    Computador > Jogador
    print('O Jogador PERDEU')