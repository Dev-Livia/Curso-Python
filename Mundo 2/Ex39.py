#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import datetime

Ano_Nasc = int(input('Informe o ano em que você nasceu: '))
Ano_Atual = datetime.now().year
Idade = Ano_Atual - Ano_Nasc

if Idade == 18:
    print('Parabéns, chegou a hora de se alistar!')
elif Idade > 18:
    print('Já se passaram {} anos, você precisa IMEDIATAMENTE fazer seu alistamento!'.format(Idade - 18))
else:
    Ano_alistamento = Ano_Nasc + 18
    print('Você ainda não chegou à idade permitida para fazer o alistamento.')
    print('Faltam {} anos para que você faça seu alistamento em {}'.format(18 - Idade, Ano_alistamento))
    print('FIQUE ATENTO!')