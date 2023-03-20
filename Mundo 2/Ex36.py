#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

Casa = float(input('Valor da casa: '))
Salario = float(input('Salario do comprador: '))
Anos = int(input('Quantos anos de financiamento? '))
Prestação = Casa / (Anos * 12)
Mínimo = Salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(Casa, Anos), end=' ')
print('A prestação será de R${:.2f}'.format(Prestação))
if Prestação <= Mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO')