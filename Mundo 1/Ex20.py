#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
print('=-=-' * 10)
print('Digite seu nome para participar do sorteio')
print('=-=-' * 10)
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
Lista = [a1, a2, a3, a4]
shuffle(Lista)
print('A ordem de apresentação será')
print(Lista)