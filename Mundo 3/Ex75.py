'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

cont = 0

for C in range (1, 5):
    Número = int(input('Digite um número: '))
    if Número == 9:
        cont += 1
print(f'O valor 9 apareceu {cont}x ')
print(f'O número 3 apareceu {Número}º posição')