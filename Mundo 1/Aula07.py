#Nessa aula, vamos aprender quais são os operadores aritméticos do Python e também sua ordem de precedência dentro de expressões matemáticas. Veja como funcionam os operadores de adição, subtração, multiplicação, divisão, exponenciação e quociente na linguagem Python.

'''nome = input('Qual é seu nome?  ')
print('Prazer em te conhecer {:=^20} !'.format(nome))'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('A soma vale {}, o produto é {} e a divisão é {:.2f}'.format(n1+n2, n1*n2, n1/n2))
print('Divisão inteira {} e potência {}'.format(n1//n2, n1**n2))
