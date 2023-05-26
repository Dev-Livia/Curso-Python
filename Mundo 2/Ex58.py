#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from time import sleep
from random import randint
cont = 0
while True:
    Jogador = int(input('Digite um número: '))
    Computador = randint(1, 10)
    print('O jogador escolheu o número {} e o Computador sorteou o número {}'.format(Jogador, Computador))
    if Computador != Jogador:
        print('Tente Novamente')
        print('==' * 20)
        cont += 1 
        sleep(1)
    else:
        break
print('Foi necessario {} palpite até o jogador acertar'.format(cont))
