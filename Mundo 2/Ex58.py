import random

print('Sou seu computador...')
print('''Acabei de pensar em um número entre 0 e 10.
        Será que você consegue adivinhar qual foi ?''')

jogador = ' '
computador = random.randint(1, 10)
acertou = False
palpites = 0
while not acertou:
        jogador = int(input('Qual seu palpite: '))
        palpites += 1
        if computador == jogador:
            acertou = True
        else:
            if computador < jogador:
                print('Menos... Tente mais uma vez.')
            elif computador > jogador:
                print('Mais... Tente mais uma vez.')
print('Acertou com {} tentativas, PARABÉNS'.format(palpites))

