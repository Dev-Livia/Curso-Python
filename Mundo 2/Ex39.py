#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

Ano_Atual = date.today().year
Nasc = int(input('Digite seu ano de nascimento: '))
Anos = Ano_Atual - Nasc
print('Você nasceu em {} e atualmente tem {} anos'.format(Nasc, Anos))

if Anos == 18:
    print('Você deve se Alistar IMEDIATAMENTE')

elif Anos < 18 :
    saldo = 18 - Anos
    print('Ainda falta {} anos para o alistamento'.format(saldo))
    ano = Ano_Atual + saldo
    print('Seu alistamento será em {}'.format(ano))
 
elif Anos > 18:
    saldo = 18 - Anos
    print('Você já deveria ter se alistado há {} anos'.format(saldo))