#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite o número para ver se ele é bissexto: '))

if ano % 4 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))