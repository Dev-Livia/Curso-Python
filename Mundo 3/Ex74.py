#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
maior = 0
menor = 0
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10)
          ,randint(0,10))
print(f'Os Valores sorteados foram: ', end = '')
for n in numeros:
    print(f'{n} ', end='')
print(f'\n O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')