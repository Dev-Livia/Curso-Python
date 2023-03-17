#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
Salario = float(input('Digite aqui o valor do seu salário: R$ '))
Aumento = (Salario + (Salario * 15 / 100))
print('Seu salário de R$ {}, com o aumento de 15% passou a ser R$ {:.2f}'.format(Salario, Aumento))