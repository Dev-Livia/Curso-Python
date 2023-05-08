#Exercício Python 3: Crie um programa que leia dois números e mostre a soma entre eles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

'''soma = n1 + n2
print('A soma entre {} + {} = {}'.format(n1,n2,soma))'''

#Também podemos otimizar esse programa como no exemplo abaixo

print('A soma entre {} + {} = {}'.format(n1, n2, (n1 + n2)))