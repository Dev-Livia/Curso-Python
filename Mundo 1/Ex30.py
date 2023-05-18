#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

número = int(input('Digite um número para ver se ele é par ou ímpar: '))

if número % 2 == 0:
    print('O número {} é PAR'.format(número))
else:
    número % 2 != 0 
    print('O número é {} ÍMPAR'.format(número))
