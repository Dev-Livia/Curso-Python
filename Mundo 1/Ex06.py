#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int(input('Digite um número: '))
print('O número digitado foi {}, o dobro desse número é {} o triplo é {}'.format(num, num * 2, num * 3))
print('A raiz quadrada é {:.2f}'.format(num ** (1/2)))