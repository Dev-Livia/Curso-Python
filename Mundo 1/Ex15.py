#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
Dia = int(input('Qual a quantidade de dias em que o carro foi alugado? '))
Km = int(input('Qual o total de Km percorridos? '))
Valor = (Dia * 60 ) + (Km * 0.15 )
print('O total a pagar é de R${}'.format(Valor))
