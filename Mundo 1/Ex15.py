#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dia = int(input('Por quantos dias o carro foi alugado ? '))
km = int(input('Qual a quantidade de Km percorrido ? '))
pagamento = ( 0.15 * km) + (60 * dia)
print('O total a pagar é de R$ {:.2f}'.format(pagamento))