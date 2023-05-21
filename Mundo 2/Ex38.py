#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
N1 = int(input('Primeiro número: '))
N2 = int(input('Segundo número: '))
print('Os Números digitados foram {} e {}'.format(N1,N2))
if N1 > N2:
    print('O PRIMEIRO valor é maior')
elif N2 > N1:
    print('O SEGUNDO valor é maior')
else:
    print('Não existe valor maior, os dois são iguais') 
