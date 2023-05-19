#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

Salário = float(input('Informe seu salário:R$ '))
if Salário > 1250:
    Aumento = Salário + (Salário * 10 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(Salário, Aumento))
if Salário <= 1250:
    Aumento = Salário + (Salário * 15 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(Salário, Aumento))