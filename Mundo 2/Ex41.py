#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
from datetime import datetime

print('----- Confederação Nacional de Natação -----')
Ano_Nasc = int(input('Digite seu ano de nascimento: '))
Idade = datetime.now().year - Ano_Nasc

if Idade <= 9:
    print('Você está classificado como atleta MIRIM.')
elif Idade <= 14:
    print('Você está classificado como atleta INFANTIL.')
elif Idade <= 19:
    print('Você está classificado como atleta JÚNIOR.')
elif Idade <= 20:
    print('Você está classificado como atleta SÊNIOR.')
else:
    print('Você está classificado como atleta MASTER.')