#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
print('Sorteio para apagar o quadro !!')
A1 = str(input('Primeiro aluno: '))
A2 = str(input('Segundo aluno:  '))
A3 = str(input('Segundo aluno:  '))
A4 = str(input('Segundo aluno:  '))
lista = [A1, A2, A3, A4]
Sorteio = choice(lista)

print('O aluno sorteado de hoje é {}'.format(Sorteio))
