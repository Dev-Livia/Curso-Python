#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
num = float(input('Digite um número para ver sua porção inteira: '))
print('O Valor digitado foi {} e sua porção inteira do número {}'.format(num, trunc(num)))