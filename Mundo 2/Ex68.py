#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print('^' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('^' * 20)


Vitoria = 0
while True:
    print('---' * 30)
    Jogador = int(input('Digite um número: '))
    pi = str(input('Par ou ímpar [P/Í]:  ')).upper().strip()
    Computador = randint(0,10 )
    soma = (Jogador + Computador) 
    rest = soma % 2
    if rest == 0 and pi == 'P':
        Vitoria += 1
        print(f'Você escolheu {Jogador} e o computador {Computador}. Total de {soma} DEU PAR')
        print('Você VENCEU')
    elif rest != 0 and pi == 'P':
        print(f'Você escolheu {Jogador} e o computador {Computador}. Total de {soma} DEU íMPAR')
        print('VOCê PERDEU')
        break
    elif rest != 0 and pi == 'I':
        Vitoria += 1
        print(f'Você escolheu {Jogador} e o computador {Computador}. Total de {soma} DEU íMPAR')
        print('VOCê VENCEU')
    if rest == 0 and pi == 'I':
        break
print(f'Você escolheu {Jogador} e o computador {Computador}. Total de {soma} ')
print(f'GAME OVER ! Você Venceu {Vitoria} Vezes')

