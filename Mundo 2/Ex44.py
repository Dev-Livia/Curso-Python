#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros

Produto = float(input('Informe o valor do produto:R$ '))
print('FORMAS DE PAGAMENTO')
print('''[ 1 ] Á vista dinheiro/cheque
         [ 2 ] Á vista no cartão
         [ 3 ] 2x no cartão
         [ 4 ] 3x no cartão''')
Opção = int(input('Qual a opção? '))

if Opção == 1:
    Total = Produto - (Produto * 10 / 100)
    print('O produto custava R${} e com o desconto de 10% passou a ser {}'.format(Produto, Total))