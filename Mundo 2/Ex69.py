'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

ContHomens = ContMulheres = ContMais18 = 0
while True:
    idade = int(input('Quantos anos voce tem ? '))
    sexo = ' '
    while sexo not in 'MF':
       sexo = str(input('Você é Homem ou Mulher [M/F]:  ')).strip().upper()
    if sexo == 'F' and idade < 20:
            ContMulheres += 1
    if sexo == 'M':
            ContHomens += 1
    if idade > 18:
            ContMais18 += 1
    opç = ' '
    while opç not in 'SN':
            opç = str(input('Deseja Continuar Cadastrando [S/N]? ')).upper()
            print('^^^^' * 15)
    if opç == 'N':
        break
print(f'Total de pessoas que são MENORES de 18: {ContMais18}')
print(f'Total de Homens que foram cadastrados: {ContHomens}')
print(f'Total de mulheres com menos de 20 anos: {ContMulheres}')


