#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
Valor_Casa = float(input('Qual o valor da casa que deseja comprar?R$ '))
Salario_Comprador = float(input('Qual o total que você ganha?R$ '))
Anos = int(input('Em quantos anos deseja pagar? '))

Prestacao_Mensal = Valor_Casa / (Anos * 12)

if Prestacao_Mensal <= Salario_Comprador * 0.3:
    print('Empréstimo APROVADO! O valor da prestação será de {:.2f} '.format(Prestacao_Mensal))
else:
    print('Emprestimo NEGADO! o valor da prestação excede 30% do salário.')