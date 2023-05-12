#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
print('REAJUSTE SALÁRIAL')
Salario = float(input('Informe seu salário:R$ '))
Reajuste = Salario + (Salario * 15 / 100)
print('O seu salário era de R${:.2f}, e com o aumento de 15% passou a ser R${:.2f}'.format(Salario, Reajuste))