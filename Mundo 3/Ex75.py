'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

Num = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print('Você digitou os valores: ', end = '')
print(f'{Num} ')
print(f'O número 9 apareceu {Num.count(9)} vezes')
if 3 in Num:
    print(f'O número 3 apareceu na {Num.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in Num:
    if n % 2 == 0:
       print(n, end=' ')