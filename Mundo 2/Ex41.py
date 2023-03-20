'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''
from datetime import date
ano = int(input('Em qual ano você nasceu? '))
ano_atual = date.today().year
Idade = ano_atual - ano 
print('Atualmente você tem {} anos então você será CLASSIFICADO COMO: '.format(Idade))
if Idade < 9:
    print('MIRIM')
elif Idade <= 14:
    print('INFANTIL')
elif Idade <= 19:
    print('JUNIOR')
elif Idade <= 25:
    print('SÊNIOR') 
else:
    Idade > 25
    print('MASTER')