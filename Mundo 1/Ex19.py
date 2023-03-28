#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
print('=-=-' * 10)
print('Digite seu nome para participar do sorteio')
print('=-=-' * 10)
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
Lista = [a1, a2, a3, a4]
sorteado = choice(Lista)
print('O aluno sorteado foi {}'.format(sorteado))