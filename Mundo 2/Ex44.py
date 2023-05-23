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
[ 4 ] 3x ou mais no cartão: 20% de juros''')
Opção = int(input('Qual a opção? '))

if Opção == 1:
    Total = Produto - (Produto * 10 / 100)
    print('O produto custava R${:.2f} e com o desconto de 10% passou a ser R${:.2f}'.format(Produto, Total))
elif Opção == 2:
    Total = Produto - (Produto * 5 / 100)
    print('O produto custava R${:.2f} e com o desconto de 5% passou a ser R${:.2f}'.format(Produto, Total))
elif Opção == 3:
    Total = Produto / 2
    print('Ao parcerlar R${:.2f} você pagará R${:.2f} agora e no próximo mês também.'.format(Produto, Total))
elif Opção == 4:
    Parcela = int(input('Em quantas vezes pretende parcelar?'))
    Total = Produto + (Produto * 20 / 100)
    mensal = Total / Parcela
    print('Sua compra será parcelada em {:.2f}x, de R${:.2f} COM JUROS '.format( Parcela, mensal))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(Produto, Total))
else: 
    print('Opção INVÁLIDA, por favor tente novamente')
