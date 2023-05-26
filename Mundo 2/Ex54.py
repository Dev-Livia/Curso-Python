#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
contM = contMenor = 0
for pessoas in range(1,8):
    Dta_Nasc = int(input('Informe seu ano de nascimento: '))
    Ano_Atual = date.today().year
    Idade =  Ano_Atual - Dta_Nasc
    if Idade >= 18:
        contM += 1
    else:
        contMenor += 1
print('===' * 20)
print('O total de pessoas que atingiram a maior idade é {}'.format(contM))
print('O total de pessoas que NÃO atingiram a maior idade é {}'.format(contMenor))
